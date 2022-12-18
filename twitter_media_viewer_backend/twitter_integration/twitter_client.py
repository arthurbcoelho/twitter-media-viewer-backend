from tweepy.user import User
from tweepy.media import Media
from tweepy.tweet import Tweet
from twitter_media_viewer_backend.models.tweet_media import TweetMedia, AttachedMedia


import tweepy
import configparser
import os
import json

config = configparser.ConfigParser()
config.read("config.ini")


API_KEY = config["twitter"]["api_key"]
API_KEY_SECRET = config["twitter"]["api_key_secret"]
ACCESS_TOKEN = config["twitter"]["access_token"]
ACCESS_TOKEN_SECRET = config["twitter"]["access_token_secret"]
BEARER_TOKEN = config["twitter"]["bearer_token"]

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

api = tweepy.API(auth)

