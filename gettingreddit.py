import praw
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')
REDDITUSERNAME=os.getenv('REDDITUSERNAME')
REDDITPASSWORD=os.getenv('REDDITPASSWORD')

reddit=praw.Reddit(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,username=REDDITUSERNAME,password=REDDITPASSWORD,user_agent='used to scrape data for educational purposes')
subreddit=reddit.subreddit('soccer')

hot_python=subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:
        print('Title:{} ups:{} downs{} have we visited {} '.format(submission.title,submission.ups,submission.downs,submission.visited))


