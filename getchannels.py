import slackclient
import os
import json

key = os.getenv('SLACK_KEY')
sc = slackclient.SlackClient(key)
userlist = {} # ul is just a name for userlist
channellist = {}#cl is just a name for channellist


#Use the channels.list api call to pull the users and add them to our channellist dictionary
def GetChannelList(cl=channellist):
    returned = sc.api_call('channels.list')
    if returned['ok'] == True:
        for channel in returned['channels']:
            cl[channel['name']] = channel
    return cl

#For each entry in the cl dictionary, print the values in a foratted way.
#User has option to change verbosity, which allows the viewiong of Channel Topics and Channel Purpose
def PrintChannelList(cl=channellist,verbose=0):
    print_statement = ''
    for channel in cl:
        print_statement = print_statement + '\nChannel: ' + str(channel) + ' ' #+ '\n' 
        for channel_attribute in sorted(cl[channel]):
            if (channel_attribute == 'topic' and verbose == 1) or (channel_attribute == 'purpose' and verbose == 1):
                #print(str(channel_attribute) + ': ')
                print_statement = print_statement + str(channel_attribute) + ': ' #+ '\n'
                for attribute_item in sorted(cl[channel][channel_attribute]):
                    print_statement = print_statement + '\t' + str(attribute_item) + ': ' + str(cl[channel][channel_attribute][attribute_item]) #+ '\n'
            elif channel_attribute == 'topic' or channel_attribute == 'purpose':
                pass
            else:
                print_statement = print_statement + str(channel_attribute) + ': ' + str(cl[channel][channel_attribute]) + ' ' #+ '\n'
    return print_statement

print(PrintChannelList(cl=GetChannelList(),verbose=1))
