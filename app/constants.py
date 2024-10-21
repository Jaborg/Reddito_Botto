from enum import Enum, auto
import os


class RedditCredentials(Enum):
    CLIENT_ID = 'CLIENT_ID'
    CLIENT_SECRET = 'CLIENT_SECRET'
    REDDIT_USERNAME = 'REDDIT_USERNAME'
    PASSWORD = 'PASSWORD'

subreddit = os.getenv('SUBREDDIT')
keyword = os.getenv('KEYWORD')
