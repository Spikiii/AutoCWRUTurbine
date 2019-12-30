#Following a tutorial from https://realpython.com/twitter-bot-python-tweepy/

import tweepy
import requests
from time import localtime, strftime

#Global variable setup
res = ""

#tweepy setup
auth = tweepy.OAuthHandler("U0n6CZW67KNy2qs2Mf3J8nxrN", "ebBiqoGZPKqsNVLwKyYT34PQkwL51lLaR8ITL2I3JZtqGTGAv5")
auth.set_access_token("1211360971412738048-4BCT5FTx2sD3XoWkZAwckQWLX2dxxp", "D07b7yCDOe7z611sEkVwN6m81KvFZC3s88cFBaluDgAkA")
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def getWindSpeed():
    #Pulling from https://home.openweathermap.org/
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=44106,us&APPID=6fe134ed57ff49a15780fc1fb0ae5953&units=imperial').json()
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
                api.update_status(t)
            if 5 <= speed <= 100:
                #t = "["+time+"]" + " WOOSH"
                t = "WOOSH"
                for i in range(1, int(speed / 2.5)):
                    t += " WOOSH"
                print(t)
                api.update_status(t)
        except Exception as e:
            print("!!Error in tweeting!!")
            print(e)
    except:
        print("!!Error in fetching wind speed!!")
        print(res)

tweet()