from reddit_bot import RedditBot


if __name__ == "__main__":
    reddit_bot = RedditBot('books','1984','How Orwellian!')
    reddit_bot.startReplyLoop()
