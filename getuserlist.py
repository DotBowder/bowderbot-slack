import slackclient
import os
import json

# You must create an environment variable with your slack api key, and then pull it into python here.
key = os.getenv('SLACK_KEY')
sc = slackclient.SlackClient(key)

userlist = {} # ul is just a name for userlist

# Use the user.list api call to pull the users and add them to our userlist dictionary.
def GetUserList(ul=userlist):
    returned = sc.api_call('users.list')
    if returned['ok'] == True:
        for member in returned['members']:
            ul[member['name']] = member
    return ul

# For each entry in the ul dictionary, print the values in a foratted way.
# Has option to hide image urls. In the "Profile" section there's a bunch of long image urls.
def PrintUserList(ul=userlist,hide_images=1):
    for user in ul:
        print('\nUser: ' + str(user))
        for user_attribute in sorted(ul[user]):
            if user_attribute == 'profile':               # the profile attribute has sub-items
                print(str(user_attribute) + ':')
                for profile_item in sorted(ul[user][user_attribute]):
                    if profile_item[0:5] == 'image' and hide_images == 1:
                        pass
                    else:
                        print('\t' + str(profile_item) + ': ' + str(ul[user][user_attribute][profile_item]))
            else:
                print(str(user_attribute) + ': ' + str(ul[user][user_attribute]))

print(GetUserList()) # Prints the user list dictionary
print(PrintUserList()) # Prints our foratted version.
