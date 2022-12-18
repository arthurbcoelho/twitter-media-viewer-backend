from fastapi import FastAPI
from twitter_media_viewer_backend.twitter_integration.tweets import get_tweet_media_list_by_twitter_username

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "oi"}

@app.get("/media/{twitter_username}")
async def get_media_from_twitter_username(twitter_username: str):
    return get_tweet_media_list_by_twitter_username(twitter_username)