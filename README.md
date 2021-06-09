# add_youtube_subscription_from_list

Playing around with the YouTube Data API to add several subscriptions from a list of channels.

NOTE: This doesn't currently work for large channel lists due to Google's quota for API method calls (searching and adding subscriptions cost quite a bit). Could get all current subscriptions first instead of searching for the ids of existing ones.

# Learnings
- Using the YouTube Data API, authentication, and other Google Developer tools
- Creating HTTP requests

# References
- https://github.com/youtube/api-samples/tree/master/python (add_subscriptions and search)
- https://developers.google.com/youtube/v3/guides/working_with_channel_ids (working with channel ids)
- https://developers.google.com/youtube/v3/docs/subscriptions/insert (inserting subscriptions)
------------------------
- https://stackoverflow.com/questions/51487195/how-can-i-use-python-google-api-without-getting-a-fresh-auth-code-via-browser-ea
(work around to requiring an access token each time to add a subscription)
- https://stackoverflow.com/questions/64847553/if-i-want-to-download-a-google-sheet-to-csv-locally-do-i-need-redirect-uris-d 
(for above link to work, need to put in redirect_uris argument in client_id.json)
------------------------
- https://stackoverflow.com/questions/37755678/retrieve-youtube-subscriptions-python-api (to get all current subscriptions)
- https://developers.google.com/youtube/v3/determine_quota_cost
