import slackclient
import os
import json
import urllib.request

key = os.getenv('SLACK_KEY')
sc = slackclient.SlackClient(key)


# This is the core function to save the images. Once you have the url_private of the image, passs it to this function, and it will save the file.
def GetImage(url):
    filename = url.split('/')[4]
    ext = url.split('/')[5].split('.')[1]
    filename = filename + '.' + ext

    headers = {}
    headers['Authorization'] = 'Bearer ' + key

    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)

    buf = res.read()

    f = open(filename, "wb")
    f.write(buf)
    f.close()


# To pull the images, we have to know the 'url_private' value of the image. I've prepared a file by pulling the chatlogs from a particular chanel, and sepparated then out line-by-line using a plugin called Beautify for the Atom code editor.
# Unless the code has been formatted with the Beautify plugin, this may not work.
def ReadFromFile(filename):
    json_data = open(files).read()
    lines = json_data.split('\n')

    for line in lines:
        try:
            if line.split(': ')[0].split("'")[1] == 'url_private':
                url = line.split(': ')[1].split("'")[1]
                GetImage(url)
        except:
            pass

# My file to read from.
#filename = 'random_2000-2999.js'
#ReadFromFile(filename)
