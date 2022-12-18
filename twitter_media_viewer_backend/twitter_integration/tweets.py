from twitter_media_viewer_backend.twitter_integration.twitter_client import client
from tweepy.user import User
from itertools import zip_longest
import json

def get_twitter_user_by_username(username: str) -> User | None:
    response = client.get_user(username=username)
    return response.data


def get_tweet_media_list_by_twitter_username(twitter_username: str):
    user = get_twitter_user_by_username(twitter_username)

    #print(json.dumps(api.get_status(1604155528858505216)._json, indent=4)) 
    tweets = client.get_users_tweets(id=user.id, exclude=['retweets', 'replies'], expansions=['attachments.media_keys'], media_fields=['duration_ms', 'url','variants'])

    pagination_token = tweets.meta['next_token']
    retrieved_tweets = tweets[0]
    retrieved_medias = tweets[1]['media']
    tweets_with_media = []
    videos = []

    for tweet in retrieved_tweets:
        if tweet.attachments:
            #tweet_media = TweetMedia(tweet_id=tweet.id, attached_media_id=tweet.attachments['media_keys'][0])
            tweet_media = {'tweet_id': tweet.id, 'attached_media_id': tweet.attachments['media_keys'][0]}
            tweets_with_media.append(tweet_media)


    for media in retrieved_medias:
        if media.type == 'video':
            # attached_media = AttachedMedia(media_id=media.media_key, medias=media.variants)
            attached_media = {'media_id': media.media_key, 'medias': media.variants}
        
            videos.append(attached_media)

    medias = [{**tweet_media, ** attached_media} for tweet_media, attached_media in zip_longest(tweets_with_media, videos, fillvalue={})]

    return {
        "pagination_token": pagination_token,
        "tweet_with_media": medias
    }
