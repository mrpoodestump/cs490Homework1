import tweepy
import yaml
import json
import sqlite3
from datetime import datetime
import pandas as pd

def makeDataBase(): 
    # establish a database connection
    conn = sqlite3.connect('tweet_example.db')
    cur = conn.cursor()
    create_tweet_info_table = """CREATE TABLE tweet_info(tweet_id BIGINT PRIMARY KEY, \
                                            user_id BIGINT, \
                                            tweet_lang TEXT, \
                                            tweet_time TEXT, \
                                            source TEXT, \
                                            tweet_text TEXT,\
                                            quote_count TEXT, \
                                            reply_count INT, \
                                            retweet_count INT,\
                                            tweet_favorite_count INT, \
                                            hashtags TEXT, \
                                            short_urls TEXT, \
                                            expanded_urls TEXT, \
                                            user_mentions TEXT);"""

    create_user_info_table =  """CREATE TABLE user_info(user_id BIGINT PRIMARY KEY, \
                                            user_screen_name TEXT, \
                                            user_name TEXT, \
                                            user_language TEXT, \
                                            location TEXT, \
                                            profile_url TEXT, \
                                            description TEXT, \
                                            protected TEXT, \
                                            verified TEXT, \
                                            created_at TEXT, \
                                            friends_count BIGINT, \
                                            followers_count BIGINT,\
                                            favorites_count BIGINT, \
                                            statuses_count BIGINT);"""

    cur.execute(create_tweet_info_table)
    cur.execute(create_user_info_table)
    conn.close()
    print("DATABASE CREATED SUCCESSFULLY")
