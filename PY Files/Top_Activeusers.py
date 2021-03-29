#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:23:34 2021

@author: germandesouza
"""

import json
import glob
import nltk
nltk.download('stopwords')
import matplotlib.pyplot as plt

##########################################################################################################################################################
###################################### (4) Top 10 most active users regarding the 23F (RT's, replies, etc.) ##############################################
##########################################################################################################################################################

tweetingpeople=[]
hello=[]
for f in glob.glob("*.json"):
    a= open(f,"r")
    b= a.read()
    result=json.loads(b)
    hello.append(result)
    
for lst in hello:
    for tweet in lst:
            data = json.dumps(tweet["user"]["screen_name"])
            tweetingpeople.append(data)
            
str1 = ''.join(tweetingpeople)
str1 = str1.replace('"',',')
print(str1)

li = list(str1.split(","))
li2=[x for x in li if x]

plt.title("Top 10 most active users on #23F")
freq = nltk.FreqDist(li2)
freq.plot(10)