import praw


subreddit=reddit.subreddit('soccer')

hot_python=subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:
        print('Title:{} ups:{} downs{} have we visited {} '.format(submission.title,submission.ups,submission.downs,submission.visited))



