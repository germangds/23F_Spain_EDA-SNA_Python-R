#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:54:34 2021

@author: germandesouza
"""

import json
import glob
import nltk
nltk.download('stopwords')
import matplotlib.pyplot as plt

##########################################################################################################################################
############################################ (2) Analyse the top 18 most popular hashtags ################################################
##########################################################################################################################################

hashtags=[]
hello=[]

for f in glob.glob("*.json"):
    a= open(f,"r")
    b= a.read()
    result=json.loads(b)
    hello.append(result)
    
for lst in hello:
    for tweet in lst:
            data = json.dumps(",".join(user['text'] for user in tweet['entities']['hashtags']))
            hashtags.append(data)

str1 = ''.join(hashtags)
str1 = str1.replace('"',',')

li = list(str1.split(","))
li2=[x for x in li if x]
res=" ".join(li2)

words2 = []
words = nltk.word_tokenize(res.lower())
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(['text', 'indices', 'rt', 'ud','amp','uff','de','persona'])
for w in words:
    if w not in stopwords and len(w) > 1:
        words2.append(w)

li=[x for x in words2 if not "\\" in x]

#Removing all hashtags which we have extracted the tweets

li = [x for x in li if x != "23f"]
li = [x for x in li if x != "venezuela"]
li = [x for x in li if x != "oeaconvzla"]
li = [x for x in li if x != "20s"]
li = [x for x in li if x != "treasure"]
li = [x for x in li if x != "dont_call_me"]
li = [x for x in li if x != "omaralas7"]

freq = nltk.FreqDist(li)
plt.title('Top 18 Hashtags 23F (Excluding #23f)')
freq.plot(18)
