#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:40:32 2021

@author: germandesouza
"""

import json
import glob
import nltk
nltk.download('stopwords')
import string
import unicodedata
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt

##########################################################################################################################################
############################################ (1) Analyse the top 10 words from our extraction ############################################
##########################################################################################################################################
#(1) Combining all data from json files and insert them in a new merged file full of texts
tweets=[]
texts_tweets=[]
for f in glob.glob("*.json"): #From the folder which we have stored all the json files, we are going to combine those tweets and make it into one list object with all the tweets which we will analyse
    a= open(f,"r")
    b= a.read()
    result=json.loads(b)
    texts_tweets.append(result)

for lst in texts_tweets: #In here we will get that list full of tweets and extract just the "text" for each tweet and store it in a global list
    for tweet in lst:
        if tweet not in tweets:
            data = json.dumps(tweet["text"])
            tweets.append(data)
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#(2) In this section we are getting that list of tweets text and spliting the different words from the different tweets. By doing this we will have a list full of words which will be necessary to determine the most popular words in the 23F. 
str1 = ''.join(tweets)
str1 = str1.replace('"',',')
li = list(str1.split(","))
li2=[x for x in li if x]
print(li2)
s = [str(i) for i in li2] 
res = "".join(s)
wordstexts_list = res.split (' ')
li3=[x for x in wordstexts_list if x]

#(3) Removing punctuation and getting rid of hashtags,URL's,usermentions and dashes. We created a punctuation list that gets rid of all the unecessary data
puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
li4=[x for x in li3 if not "\\" in x]
li5=[x for x in li4 if not "@" in x]
li6=[x for x in li5 if not "/" in x]
li7=[x for x in li6 if not "-" in x]
li8=[x for x in li7 if not "#" in x]
li9=[x for x in li8 if not "'" in x]
s2= [str(i) for i in li9] 
res2 = " ".join(s2)

#(4) Getting rid off all the rest of unecessary data that can be found in the list of tweet words
p = string.punctuation
table_p = str.maketrans(p, len(p) * " ")
a=res2.translate(table_p)
d = string.digits
table_d = str.maketrans(d, len(d) * " ")
c=a.translate(table_d)
print(c)

#(5) created two different list of frequent words to show the effectiveness of stopwords
words2 = []
words = nltk.word_tokenize(c.lower())
stopwords = nltk.corpus.stopwords.words('spanish')
#This step very important, as you will have to errase all data that is considered as a stopword but is not detected by the stopword list
p=["pueblo venezolano","venezolano","a","abans","ací","ah","així","això","al","aleshores","algun","alguna","algunes","alguns","alhora","allà","allí","allò","als","altra","altre","altres","amb","ambdues","ambdós","anar","ans","apa","aquell","aquella","aquelles","aquells","aquest","aquesta","aquestes","aquests","aquí","baix","bastant","bé","cada","cadascuna","cadascunes","cadascuns","cadascú","com","consegueixo","conseguim","conseguir","consigueix","consigueixen","consigueixes","contra","d'un","d'una","d'unes","d'uns","dalt","de","del","dels","des","des de","després","dins","dintre","donat","doncs","durant","e","eh","el","elles","ells","els","em","en","encara","ens","entre","era","erem","eren","eres","es","esta","estan","estat","estava","estaven","estem","esteu","estic","està","estàvem","estàveu","et","etc","ets","fa","faig","fan","fas","fem","fer","feu","fi","fins","fora","gairebé","ha","han","has","haver","havia","he","hem","heu","hi","ho","i","igual","iguals","inclòs","ja","jo","l'hi","la","les","li","li'n","llarg","llavors","m'he","ma","mal","malgrat","mateix","mateixa","mateixes","mateixos","me","mentre","meu","meus","meva","meves","mode","molt","molta","moltes","molts","mon","mons","més","n'he","n'hi","ne","ni","no","nogensmenys","només","nosaltres","nostra","nostre","nostres","o","oh","oi","on","pas","pel","pels","per","per que","perquè","però","poc","poca","pocs","podem","poden","poder","podeu","poques","potser","primer","propi","puc","qual","quals","quan","quant","que","quelcom","qui","quin","quina","quines","quins","què","s'ha","s'han","sa","sabem","saben","saber","sabeu","sap","saps","semblant","semblants","sense","ser","ses","seu","seus","seva","seves","si","sobre","sobretot","soc","solament","sols","som","son","sons","sota","sou","sóc","són","t'ha","t'han","t'he","ta","tal","també","tampoc","tan","tant","tanta","tantes","te","tene","tenim","tenir","teniu","teu","teus","teva","teves","tinc","ton","tons","tot","tota","totes","tots","un","una","unes","uns","us","va","vaig","vam","van","vas","veu","vosaltres","vostra","vostre","vostres","érem","éreu","és","éssent","últim","ús"]
def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    return str(text)

test=[]
for i in p:
    test.append(strip_accents(i))
####################################################################################################################
stopwords.extend(test)
for w in words:
    if w not in stopwords and len(w) > 1:
        words2.append(w)
freq = nltk.FreqDist(words)
freq2 = nltk.FreqDist(words2)
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#6.1) Here you will find the two diagrams with stop words and without stop words
plt.title("Top 20 Most Frequent Words in 23F (Tuesday 23rd 2021)")
freq2.plot(20)

#6.2) Wordcloud
outfile= open("wordcloud.txt","w")
words2 = [x for x in words2 if x != "venezolano"]
for item in words2:
    out_string= "{} ".format(item)
    outfile.write(out_string)
datacloud= open("wordcloud.txt").read()
wordcloud = WordCloud(background_color='white').generate(datacloud)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("wordcloud_23F.png")

#6.3) sentiment analysis
subj = []
pol= []
sentimentwords = open("Wordcloudtext_Sinvenezolano_English.txt").read() # In this segment of the code we had to translate the "wordcloud.txt" into this website https://www.onlinedoctranslator.com/app/translationprocess to get all the words translated. This is helpful in using textblob sentiment capabilities.
sentimentwords = list(sentimentwords.split(" "))
for s in sentimentwords:
    tb = TextBlob(s)
    subj.append(tb.sentiment.subjectivity)
    pol.append(tb.sentiment.polarity)

plt.hist(subj, bins=10)
plt.xlabel('subj score')
plt.ylabel('tweet count')
plt.title('Subjectivity Distribution 23F')
plt.grid(True)
plt.show()
    
plt.hist(pol, bins=10)
plt.xlabel('pol score')
plt.ylabel('tweet count')
plt.title('Polarity Distribution 23F')
plt.grid(True)
plt.show()
    
avg_subj= sum(subj)/len(pol)
avg_pol= sum(pol)/len(subj)
print("The average of subjectivity is {} and the average of polarity is {}".format(avg_subj,avg_pol))