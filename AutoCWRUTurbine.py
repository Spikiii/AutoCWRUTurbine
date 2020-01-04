#Following a tutorial from https://realpython.com/twitter-bot-python-tweepy/

import tweepy
import requests
from time import localtime, strftime

#Global variable setup
res = ""
idPath = "IDs.txt"

#Fetching IDs from a text file located at idPath
#Make sure that it is 1 ID per line, and an extra line break after weatherID
ids = []
with open(idPath) as f:
    for line in f:
        ids.append(line[:-1])
tID1 = ids[0]
tID2 = ids[1]
tID3 = ids[2]
tID4 = ids[3]
weatherID = ids[4]

#tweepy setup
auth = tweepy.OAuthHandler(tID1, tID2)
auth.set_access_token(tID3, tID4)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def getWindSpeed():
    #Pulling from https://home.openweathermap.org/
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=44106,us&APPID='+weatherID+'&units=imperial').json()
    return res['wind']['speed']

def tweet():
    try:
        speed = getWindSpeed()
        print(speed)
        try:
            time = strftime("%I:%M %p", localtime())
            if 0 <= speed < 5:
                #t = "["+time+"]" + " No WOOSH :("
                t = "No WOOSH :("
                print(t)
                #api.update_status(t)
            if 5 <= speed <= 100:
                #t = "["+time+"]" + " WOOSH"
                t = "WOOSH"
                for i in range(1, int(speed / 2.5)):
                    t += " WOOSH"
                print(t)
                #api.update_status(t)
        except Exception as e:
            print("!!Error in tweeting!!")
            print(e)
    except:
        print("!!Error in fetching wind speed!!")
        print(res)

tweet()