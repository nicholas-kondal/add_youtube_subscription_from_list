# This code executes a search request for the specified search term.
# NOTE: You must provide a developer key obtained in the Google APIs Console.

import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set DEVELOPER_KEY to the API key value from the APIs & Services > Credentials apps tab of https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = ''

def youtube_search(channel_name='Google', max_results=100000):
  youtube = build(serviceName='youtube', version='v3', developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified query term.
  search_response = youtube.search().list(q=channel_name, part='id,snippet', maxResults=max_results).execute()

  channels = {}
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#channel':
      channels[search_result['snippet']['title']] = search_result['id']['channelId']

  # Returns either the channel id if the requested channel name is in the dictionary, 
  # or just the channel name if the channel wasn't found.
  if channels == {}:
    return channel_name
  else:
    for channel_key in channels.keys():
      if channel_name.lower() == channel_key.lower():
        return channels[channel_key]
    return channel_name

if __name__ == '__main__':
  try:
    channel_id = youtube_search(channel_name = 'Google', max_results = 25)
  except HttpError as e:
    print(f'An HTTP error {e.resp.status} occurred: {e.content}')