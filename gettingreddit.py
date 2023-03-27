import praw
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')
REDDITUSERNAME=os.getenv('REDDITUSERNAME')
REDDITPASSWORD=os.getenv('REDDITPASSWORD')

reddit=praw.Reddit(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,username=REDDITUSERNAME,password=REDDITPASSWORD,user_agent='used to scrape data for educational purposes')
#for submission in reddit.front.hot():   for hot posts on the front page
   # print(submission)

###########################################################

subreddit=reddit.subreddit('neoliberal')


'''
hot_posts=subreddit.hot(limit=3)

for submission in hot_posts:
    if not submission.stickied:
       #print('Title:{} ups:{} downs{} have we visited {} '.format(submission.title,submission.ups,submission.downs,submission.visited))
       
       #submission.comments.list() creates a breath first search of comments
       #to remove the 'more comments' tag and replace it with actual replies , use
       # submission.comments.replace_more(limit=None)    //remove the 'more comments' tag 
       # comment in submission.comments.list():   //then convert it into a list and loop through it
       #    //inside the for loop 
       # However,comments are so deep, so it takes a lot of data to parse if it is a large comment section
        comments=submission.comments.list()    #convert the comments into a list
        for comment in comments:               # loop through
            print('Parent Id',comment.parent())
            print('Comment',comment.id)
            print(comment.body)

           # if len(comment.replies)>0:
            #    for reply in comment.replies:
            #        print('REPLY',reply.body)

            
            '''

####################################################
            
for comment in subreddit.stream.submissions():
    try:
        print(comment.body)
    except Exception as e:
        pass




