#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:42:54 2021

@author: germandesouza
"""

import json
import glob
import csv
import pandas

tweets=[]
texts_tweets=[]

#From the folder which we have stored all the json files, we are going to combine those tweets and make it into one list object with all the tweets which we will analyse
for f in glob.glob("*.json"): 
    a= open(f,"r")
    b= a.read()
    result=json.loads(b)
    texts_tweets.append(result)

#In here we will get that list full of tweets and extract just the "text" for each tweet and store it in a global list
for lst in texts_tweets: 
    for tweet in lst:
        if tweet not in tweets: #This line of code is in charge of getting rid of all the duplicates that we may have and it appends it into a list of tweets called "tweets"
            tweets.append(tweet)

#This block of code enables to change the "tweets" list to a dataframe. This will be useful to extract the information that we really need and export it into a excel file. This excel file will help us to execute our main SNA 
df= pandas.DataFrame(tweets) 
df2 = df[["id_str","created_at","text"]]
df2.to_excel("allreytweets_3.xlsx", index=False)


#We need this block of code to combine all the tweets information into one file
with open(("alltweets23F.json"), 'w') as outfile:
    json.dump(tweets, outfile, indent=4)