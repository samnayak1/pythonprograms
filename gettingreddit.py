import praw

reddit=praw.Reddit(client_id='RxejSsjn5UJMVEV0mWjN5A',client_secret='ETfmg7y0_O0j2JcmYc3IDGVBP0mk9A',username='samnayak1',password='Grifter123',user_agent='used to scrape data for educational purposes')

subreddit=reddit.subreddit('soccer')

hot_python=subreddit.hot(limit=5)

for submission in hot_python:
    if not submission.stickied:
        print('Title:{} ups:{} downs{} have we visited {} '.format(submission.title,submission.ups,submission.downs,submission.visited))



