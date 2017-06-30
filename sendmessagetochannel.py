import slackclient
import os
import json

key = os.getenv('SLACK_KEY')
sc = slackclient.SlackClient(key)

#Send a text message to a channel
def SendTextMessage(channel,text):
    sc.api_call('chat.postMessage',channel=channel,text=text,reply_broadcast=True)

channel = 'channel id here'
message = 'Message to send to channel'
SendTextMessage(channel, message)
