import logging
import time

from reddit_bot import RedditBot
from constants import subreddit, keyword


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    while True:
        reddit_bot = RedditBot(subreddit, keyword)
        reddit_bot.startReplyLoop()
        logging.info("Breaking for a while")
        time.sleep(30)
