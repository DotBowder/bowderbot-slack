import slackclient
import os
import json

key = os.getenv('SLACK_KEY')
sc = slackclient.SlackClient(key)

def GetChatLog(channel,latest, count=1000):
    return sc.api_call('channels.history', channel=channel, latest=latest, count=count)

channelid = 'place id here'
latesttimestamp = 1480544737.000002
print(GetChatLog(channelid, latesttimestamp, count=1000))
