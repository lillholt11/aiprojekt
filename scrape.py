import gpt_2_simple as gpt2
import praw

title = []
body = []

reddit = praw.Reddit(client_id = "vvT6zwSKNTzn7g", 
                     client_secret = "lLSIepmEv64ezqLpncuaSSCk-c8",     
                     user_agent = "unpopular_bot", 
                     username = "abblinkas", 
                     password = "qwerty123")

unpopularopinion = reddit.subreddit('unpopularopinion').top(limit=1000)

def scrape():
    for submission in unpopularopinion:
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
    
scrape()