#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:34:00 2019

@author: germandesouza
"""

from twython import TwythonStreamer
import json
import time
import sys

# https://twython.readthedocs.io/en/latest/usage/streaming_api.html In collaboration of Gene Lee
class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:     
            tweets.append(data) 
            print(len(tweets), data, sep="\n")   

        if len(tweets) >= 1000:  
            self.disconnect()   


    def on_error(self, status_code, data):
        print(status_code)
        self.disconnect()


if len(sys.argv) > 1:
    keyword = sys.argv[1]
else:
    keyword = 'happy'

tweets = []

stream = MyStreamer('Ur9pSBt0z6v96vSqSiuRXgHVN','Q6Mz1p9W1W90sQY8h3LpjOm73P11oQzfngOngQhs6ZJzMQVojf', '1107791419618426880-yiLzwktV6pxcs4JaXYmQ43y5bNXQ7q', '7ycm2ck5ksGxM2vKsNTJJs5vW9cHoXxwtKZAFhIdgaZV0')

stream.statuses.filter(track="CulturaSegura")

timestr = time.strftime("%Y|%m|%d-%H:%M:%S")
with open(("23F"+timestr), 'w') as outfile:
    json.dump(tweets, outfile, indent=4)
    
