#Reddit bot created by Linus Kasper

import gpt_2_simple as gpt2
import time
import random
import tarfile
import requests
import os
import praw
from datetime import datetime, timedelta

#praw libraries necessary information
reddit = praw.Reddit(client_id = "vvT6zwSKNTzn7g", 
                     client_secret = "lLSIepmEv64ezqLpncuaSSCk-c8",     
                     user_agent = "unpopular_bot", 
                     username = "abblinkas", 
                     password = "qwerty123")

#model name and location
tarFilepath = "checkpoint_run1.tar"
tarGoogleFileid = "1ZC3fGu4EOMcOmmKK3ug6dJ3gBWvRMDXn"
dataFilepath = "data.txt"
dataGoogleFileid = "1t43abHqeBzuKwoLh4zCybXXze_2-gbFb"

#function to scrape a subreddit to create the data.txt file
def scrape():
    for submission in reddit.subreddit('unpopularopinion').top(limit=1000):
        title.append(submission.title)
        body.append(submission.selftext)

    file = open("data.txt", "w")

    for i in range(len(title)):
        try:
            titletext = title[i].replace("\n", " ")
            bodytext = body[i].replace("\n", " ")
            file.write(titletext + "*" * 30  + bodytext + "\n")
        except:
            pass

#function to extract files from tarfile
def extract():
    with tarfile.open(tarFilepath, 'r') as tar:
        tar.extractall()
    os.remove(tarFilepath)
    print("File",tarFilepath, "Removed!")

#dowloading model file from google
def download_file_from_google_drive(id, destination):

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    def save_response_content(response, destination):
        with open(destination, "wb") as f:
            for chunk in response.iter_content(32768):
                if chunk:
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

download_file_from_google_drive(tarGoogleFileid,tarFilepath)
extract()
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
download_file_from_google_drive(dataGoogleFileid,dataFilepath)

#checking whether post exist already
def checkPost(post):
    print("Checking post...")
    with open('data.txt') as f:
        for posts in f.readlines():
            if post in posts:
                return True
    return False

#generating posts
def generatePost():
    #generating multiple posts
    print("Generating posts...")
    rawPosts = gpt2.generate(sess, return_as_list=True)[0]
    posts = rawPosts.split("\n")
    acceptablePosts = []
    #appending acceptable posts to an array
    for post in posts:
        if "******************************" in post and not checkPost(post):
            acceptablePosts.append(post.split("******************************"))
    if len(acceptablePosts) == 0:
        print("No possible posts found. Trying again...")
        return generate_text()
    else:
        #returning the best (shortest) post
        post = min(acceptablePosts, key=len)
        bestPost = {"title": post[0].replace("\\", ""), "body": post[1].replace("\\", "")}
        print("Generation of an acceptable post done")
        return bestPost

#posting the post to a subreddit
def post(title, body, now):
    try:
        reddit.subreddit("BotsParadise").submit(title, selftext=body)
        print('Successfully posted at', now)
    except:
        print('Post failed')

while True:    
    now = datetime.now()
    bestPost = generatePost()
    post(bestPost["title"], bestPost["body"], now)
    sleeptime = 3600 # 3600s = 1 hour
    deltaTime = now + timedelta(seconds=sleeptime)
    print("Next tweet will be in ",str(timedelta(seconds=sleeptime)), " at " , deltaTime )
    #sleeping 1 hour until next post
    time.sleep(sleeptime)
