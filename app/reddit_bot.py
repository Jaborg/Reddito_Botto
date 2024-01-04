import praw
import time
import logging
import os


from text_analysis import get_sentiment_score,calculate_mean
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
        sentiment_score = []
        for comment in subreddit_object.stream.comments():
            if self.trigger_phrase in comment.body:
                sentiment = get_sentiment_score(comment.body)
                sentiment_score.append(sentiment)
                mean_so_far = calculate_mean(sentiment_score)

                logging.info("Comment identified")
                logging.info(f"The comment which contains {self.trigger_phrase} is: \n {comment.body} ")
                logging.info(f"\n The sentiment score is which contains {sentiment} ")
                logging.info(f"\n The overall sentiment score for comments with {self.trigger_phrase} in {self.subreddit_name} is: \n {mean_so_far} ")
                time.sleep(5)
        
    
            logging.info(f'Going through comment {count}...')
            count += 1
            

    def stopReplyLoop(self):
        
        return

