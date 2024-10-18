import logging

from reddit_bot import RedditBot


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    reddit_bot = RedditBot('worldnews','Trump','How Orwellian!')
    reddit_bot.startReplyLoop()
