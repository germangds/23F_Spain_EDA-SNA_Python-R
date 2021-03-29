#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:34:50 2021

@author: germandesouza
"""

import json
import glob
import nltk
nltk.download('stopwords')

replycount=[]
hello=[]
influence_score= []
raw_text= []

for f in glob.glob("*.json"):
    a= open(f,"r")
    b= a.read()
    result=json.loads(b)
    hello.append(result)

for lst in hello:
    for tweet in lst:
        if 'retweeted_status' in tweet:
            data = tweet['retweeted_status']
            count = ((int(data['is_quote_status']))+data['retweet_count'] + data['favorite_count'])
            influence_score.append(count)
        else:
            influence_score.append(0)
   
for lst in hello:
    for tweet in lst:
            text = tweet['text']
            raw_text.append(text)

zz=max(influence_score)
zzz=influence_score.index(zz)
print("The most famous influential tweet according to our retweeted_status function is the following:\n{} ".format(raw_text[zzz]))

