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

hot_posts=subreddit.hot(limit=3)

for submission in hot_posts:
    if not submission.stickied:
       #print('Title:{} ups:{} downs{} have we visited {} '.format(submission.title,submission.ups,submission.downs,submission.visited))
        comments=submission.comments.list()
        for comment in comments:
            print('Parent Id',comment.parent())
            print('Comment',comment.id)
            print(comment.body)

           # if len(comment.replies)>0:
            #    for reply in comment.replies:
            #        print('REPLY',reply.body)

