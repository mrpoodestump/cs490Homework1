import tweepy
from python.cs491.apiConfig.getCreds import getCreds
from python.cs491.dataBase.makeDataBase import makeDataBase
from python.cs491.dataBase.doesTableExist import doesTableExist
from python.cs491.dataBase.makeStreamListenerObject import MyStreamListener

api = getCreds() 
try: 
    makeDataBase() 
except Exception as e: 
    print('Data base already exists: {e}')
doesTableExist()

myStreamListener = MyStreamListener(listen_time=30)
myStream = tweepy.Stream(api.auth, myStreamListener)

keywords= ['#gabbypetito']

try: 
    print('Stream Filter')
    myStream.filter(track=keywords)
    print('DONE')
except Exception as e: 
    print(f"error in stream filter {e}")
