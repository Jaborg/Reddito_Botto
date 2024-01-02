import praw
import time
import logging
import os

from secrets import RedditCredentials

class RedditBot:

    def __init__(self,subreddit_name,trigger_phrase,response):
    
        self.subreddit_name = subreddit_name
        self.trigger_phrase = trigger_phrase
        self.response = response
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


    def startReplyLoop(self):
        # Main loop
        subreddit_object = self.identifySubreddit()
    
        logging.info(f'Bot is now active in r/{self.subreddit_name}')
        count = 0
        for comment in subreddit_object.stream.comments():
            if self.trigger_phrase in comment.body:
                logging.info("Comment identified")
                # Reply to the comment
                reply_text = "How Orwellian!"
                logging.critical(f"The comment which contains {self.trigger_phrase} is {comment.body} ")
                # comment.reply(reply_text)
                # logging.critical(f'Replied to comment by {comment.author} in r/{self.subreddit_name}')
    
            logging.critical(f'Going through comment {count}...')
            time.sleep(1)
            count += 1
            

    def stopReplyLoop(self):
        
        return
