import tweepy
import yaml
import json
import sqlite3
from datetime import datetime
import pandas as pd

# yaml file reader funtion
def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def getCreds(): 
    # yaml config file path
    file_path = './python/cs491/apiConfig/twitter_api_key_config.yaml'
    # read from config file
    api_credential = read_yaml(file_path)


    # API authentication
    auth = tweepy.OAuthHandler(api_credential["api_key"], \
                            api_credential["api_secret_token"])
    auth.set_access_token(api_credential["access_token"], \
                        api_credential["access_token_secret"])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api