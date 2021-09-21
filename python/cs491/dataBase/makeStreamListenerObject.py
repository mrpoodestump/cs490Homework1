from datetime import datetime
import sqlite3
import json
import pandas as pd
import tweepy
import time
# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, listen_time=60):
        super(MyStreamListener, self).__init__()
        self.counter = 0
        print("Initialized Tweepy StreamListener.")
        self.start_time = datetime.now()
        self.current_time = datetime.now()
        self.listen_time = listen_time
        self.unique_user_id_set = set([])
        # adding database connection code
        self.conn = sqlite3.connect('tweet_example.db')
        self.cur  = self.conn.cursor()
        
    def insert_data(self, data):
        tweet_object=json.loads(data) # convert "string-line" into json
        # check if json object has a key id. Otherwise continue to next.
        if 'id' in tweet_object.keys(): 
            
            # tweet object information
            tweet_id        = tweet_object['id']
            user_id         = tweet_object['user']['id']
            tweet_lang      = tweet_object['lang']
            tweet_time      = str(pd.to_datetime(tweet_object['created_at']))
            source          = tweet_object['source']
            tweet_text      = tweet_object['text']

            # tweet numeric information
            quote_count = tweet_object['quote_count']
            reply_count = tweet_object['reply_count']
            retweet_count = tweet_object['retweet_count']
            tweet_favorite_count = tweet_object['favorite_count']

            # meta-content information
            hashtags = [str(hashtag['text']) for hashtag in tweet_object['entities']['hashtags']]
            hashtags = ",".join(hashtags)
            short_urls = [str(url['url']) for url in tweet_object['entities']['urls']]
            short_urls = ",".join(short_urls)
            expanded_urls = []
            try:
                expanded_urls = [str(url['expanded_url']) for url in tweet_object['entities']['urls']]
            except:
                print('Error Message: No Expanded URL.')
            expanded_urls = ",".join(expanded_urls)

            # user interaction based informations    
            user_mentions = [str(user_mentions['id'])\
                        for user_mentions in tweet_object['entities']['user_mentions']]
            user_mentions = ",".join(user_mentions)

            tweet_info = (tweet_id, user_id, tweet_lang,\
                    tweet_time, source, tweet_text,\
                    quote_count, reply_count, retweet_count,\
                    tweet_favorite_count, hashtags, short_urls,\
                    expanded_urls, user_mentions)
            self.cur.execute("INSERT INTO tweet_info \
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", tweet_info)
            
            # user profile information

            if user_id in self.unique_user_id_set:
                pass
            else:
                self.unique_user_id_set.add(user_id)
                
                user_screen_name      = tweet_object['user']['screen_name']
                user_name             = tweet_object['user']['name']
                user_language         = tweet_object['user']['lang']  
                location              = tweet_object['user']['location']
                profile_url           = tweet_object['user']['url']
                description           = tweet_object['user']['description']
                protected             = tweet_object['user']['protected']
                verified              = tweet_object['user']['verified']
                created_at            = str(pd.to_datetime(tweet_object['user']['created_at']))
                friends_count         = tweet_object['user']['friends_count']
                followers_count       = tweet_object['user']['followers_count']
                favorites_count       = tweet_object['user']['favourites_count']
                statuses_count        = tweet_object['user']['statuses_count']

                user_information = (user_id, user_screen_name, user_name,\
                       user_language, location, profile_url,\
                       description, protected, verified, created_at,\
                       friends_count, followers_count,\
                       favorites_count, statuses_count)
                self.cur.execute(" INSERT INTO user_info VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user_information)
            
            self.conn.commit()
        
    def on_data(self, data):
        self.current_time = datetime.now()
        time_elapsed = (self.current_time - self.start_time).total_seconds()
        if self.counter < 100000:
            try:
                self.counter += 1
                """
                Changing the code here.
                Previously, we saved to Text file.
                Now, we will pass this to the Database insertor method.
                """
                # -- self.output_file.write(str(data))
                print(f"Tweet Processed: {self.counter}\n")
                self.insert_data(str(data))
                
            except Exception as e:
                print(f"On data Exception:{e}.")
        else:
            print(f"Stream listen counter reached. Total listen time: {self.listen_time} seconds.\n\n")
            print(f"Total Tweet processed: {self.counter}")
            self.conn.close()
            return False

    # handling Errors
    def on_error(self, status_code):
        print(f"status_code: {status_code}")
        if status_code == 420:
            time.sleep(16 * 60)
            #returning False in on_error disconnects the stream
            return True