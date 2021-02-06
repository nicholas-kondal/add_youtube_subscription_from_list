from search_for_channel import youtube_search
from add_subscription import get_authenticated_service, add_subscription
from googleapiclient.errors import HttpError

youtube = get_authenticated_service()
# request = youtube.subscriptions().list(part="snippet,contentDetails", mine=True)
# subscriptions_list = request.execute()
# print(subscriptions_list)

CHANNEL_LIST = '.txt' # one channel on each line

channel_file = open(CHANNEL_LIST, encoding='utf8')
channels = channel_file.read().splitlines()

channel_lists = {}
channel_lists['channels_not_found'] = []
channel_lists['channels_already_added'] = []
channel_lists['channels_now_added'] = []

for i, channel in enumerate(channels):
    channel_id = youtube_search(channel)
    if channel_id == channel:
        channel_lists['channels_not_found'].append(channel)
    else:
        try:
            add_subscription(youtube, channel_id)
        except HttpError:
            channel_lists['channels_already_added'].append(channel)
        else:
            channel_lists['channels_now_added'].append(channel)
    if i % 10 == 0:
        print(f"{len(channel_lists['channels_now_added'])} added, {len(channel_lists['channels_already_added'])} already added, {len(channel_lists['channels_not_found'])} not found")

for list in channel_lists.keys():
    with open(list+'.txt', 'w') as output:
        for line in channel_lists[list]:
            s = "".join(map(str, line))
            output.write(s+'\n')