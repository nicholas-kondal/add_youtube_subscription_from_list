# This code adds a channel subscription. 

import argparse
import os
import re

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains the OAuth 2.0 information for this application, including its client_id and client_secret. 
# You can acquire an OAuth 2.0 client ID and client secret from the Google Cloud Console at https://cloud.google.com/console. 
# Please ensure that you have enabled the YouTube Data API for your project. 
# For more information about using OAuth2 to access the YouTube Data API, see https://developers.google.com/youtube/v3/guides/authentication. 
# For more information about the client_secrets.json file format, see https://developers.google.com/api-client-library/python/guide/aaa_client_secrets.
CLIENT_SECRETS_FILE = 'client_id.json'

# This OAuth 2.0 access scope allows for full read/write access to the authenticated user's account.
SCOPES = ['https://www.googleapis.com/auth/youtube']

def get_authenticated_service():
    credential_path = os.path.join(os.getcwd(), 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    # This will open an authorisation screen for one time to store credentials 
    # so that you don't need to keep authorising for each channel.
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
        credentials = tools.run_flow(flow, store)
    return build(serviceName='youtube', version='v3', credentials=credentials)

# This method calls the API's youtube.subscriptions.insert method to add a subscription to the specified channel.
def add_subscription(youtube, channel_id, return_response=False):
  add_subscription_response = youtube.subscriptions().insert(part='snippet', body=dict(snippet=dict(resourceId=dict(channelId=channel_id)))).execute()
  if return_response:
    return add_subscription_response['snippet']['title']

if __name__ == '__main__':
  youtube = get_authenticated_service()
  try:
    channel_title = add_subscription(youtube, channel_id='UC_x5XG1OV2P6uZZ5FSM9Ttw', return_response=True) # GoogleDevelopers YT channel
  except HttpError as e:
    print(f'An HTTP error {e.resp.status} occurred: {e.content}')
  else:
    print(f'A subscription to {channel_title} was added.')