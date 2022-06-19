#Following a tutorial from https://realpython.com/twitter-bot-python-tweepy/

import tweepy
import requests
from datetime import datetime
from time import localtime, strftime

#Global variable setup
res = ""
idPath = ".autoCWRU.conf"

#Fetching IDs from a text file located at idPath
#Make sure that it is 1 ID per line, and an extra line break after weatherID
ids = []
with open(idPath) as f:
    for line in f:
        ids.append(line[:-1])
consumer_token = ids[0]
consumer_secret = ids[1]
auth_key = ids[2]
auth_access_token = ids[3]
weatherID = ids[4]

print("================================================================================")
print("Running AutoCWRUTurbine.py at %s" % datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

#tweepy setup
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(auth_key, auth_access_token)
api = tweepy.API(auth)

try:
        api.verify_credentials()
        print("Authentication OK")
except:
        print("Error during authentication")

def getWindSpeed():
        print("Fetching wind speed from https://home.openweathermap.org/")
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=44106,us&APPID=%s&units=imperial' % weatherID).json()
        print("Successfully got wind speed!")
        return res['wind']['speed']

def tweet():
        speed = getWindSpeed()
        print("Current wind speed in Cleveland, OH: %smph" % speed)
        time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        if 0 <= speed < 5:
                t = "No WOOSH :("
                print("Attempting to tweet '%s'" % t)
                print(api.update_status(t))
                print("Tweeting success!")
        if 5 <= speed <= 100:
                t = "WOOSH"
                for i in range(1, int(speed / 2.5)):
                        t += " WOOSH"
                print("Attempting to tweet '%s'" % t)
                print(api.update_status(t))
                print("Tweeting success!")

tweet()