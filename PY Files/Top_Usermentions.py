#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:17:39 2021

@author: germandesouza
"""

import json
import glob
import nltk
nltk.download('stopwords')
import matplotlib.pyplot as plt

#########################################################################################################################################
############################################ (3) Analyse the top 9 most popular user mentioned ##########################################
#########################################################################################################################################

usermentions=[]
hello=[]
for f in glob.glob("*.json"):
    a= open(f,"r")
    b= a.read()
    result=json.loads(b)
    hello.append(result)
    
for lst in hello:
    for tweet in lst:
            data = json.dumps(",".join(user['screen_name'] for user in tweet['entities']['user_mentions']))
            usermentions.append(data)
            
str1 = ''.join(usermentions)
str1 = str1.replace('"',',')
print(str1)

li = list(str1.split(","))
li2=[x for x in li if x]

plt.title("Top 9 User Mentions in #23F")
freq = nltk.FreqDist(li2)
freq.plot(9)
