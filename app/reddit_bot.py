import praw
import time
import logging
import os

from prawcore.exceptions import ResponseException

from constants import RedditCredentials
from gen_ai_utils import AI_Response


class RedditBot:

    def __init__(self,subreddit_name,trigger_phrase):
    
        self.subreddit_name = subreddit_name
        self.trigger_phrase = trigger_phrase
        self.client_id = os.environ.get(RedditCredentials.CLIENT_ID.value)
        self.client_secret = os.environ.get(RedditCredentials.CLIENT_SECRET.value)
        self.reddit_username = os.environ.get(RedditCredentials.REDDIT_USERNAME.value)
        self.password = os.environ.get(RedditCredentials.PASSWORD.value)
        self.user_agent = "Bot for Jaborg"

    def createInstance(self):
        reddit_instance = praw.Reddit(
            client_id = self.client_id,
            client_secret = self.client_secret,
            username = self.reddit_username,
            password = self.password,
            user_agent = self.user_agent,
        )
        return reddit_instance
    
    def identifySubreddit(self):
        reddit = self.createInstance()
        subreddit_object = reddit.subreddit(self.subreddit_name)
        return subreddit_object
    
    def checkPostAlreadyMade(self):
        pass

    def generateResponsetoPost(self,title_of_submission):
        response = AI_Response(title_of_submission,'Make a casual comment about this topic, lamenting the erosion of American democracy, keep it under 75 words')
        return response.create_response()
    
    def startReplyLoop(self):
        # Main loop
        subreddit_object = self.identifySubreddit()
        logging.info(f'Bot is now active in r/{self.subreddit_name}')
        batch_posts = []
        for submission in subreddit_object.new(limit=25):
            batch_posts.append(submission.title)
            if self.trigger_phrase in submission.title:
                logging.info("Post identified")
                logging.info(f"The post which contains {self.trigger_phrase} is: \n {submission.title} \n ")
                response = self.generateResponsetoPost(submission.title)
                logging.info('Commenting' , response)
                submission.reply(response)
                break
        logging.info(batch_posts)
        
            

    def stopReplyLoop(self):
        
        return

