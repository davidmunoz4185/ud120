#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "..\\tools\\" )
#path = os.path.join('../tools/', path[:-1])
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""

"""
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
string1 = ""
string2 = ""
string3 = ""

email_list = [string1, string2, string3]
bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)
print vectorizer.vocabulary_.get("great")

import nltk
import nltk.download()
from nltk.corpus import stopwords
sw = stopwords.words("english")

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("responsiveness")
stemmer.stem("responsivity"
stemmer.stem("unresponsivity")
"""

from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter < 2000000:
            # old line
            # print os.path.join('..', path[:-1])
            #path = os.path.join('..', path[:-2] + '.')
            path = os.path.join('..', path[:-1])
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            content = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            replace_words = ["sara", "shackleton", "chris", "germani"]
            for w in replace_words:
                content = content.replace(w, "")

            ### append the text to word_data
            word_data.append(content)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "Sara":
                from_data.append("0")
            else:
                from_data.append("1")

            email.close()

print
"emails processed"
from_sara.close()
from_chris.close()

print
len(from_data)

print('******************')
print('content after processing')
print("word_data[152]= ", word_data[152])
print('******************')

pickle.dump(word_data, open("your_word_data.pkl", "w"))
pickle.dump(from_data, open("your_email_authors.pkl", "w"))

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from collections import Counter

vectorizer = TfidfVectorizer(stop_words="english")

x_tfidf = vectorizer.fit_transform(word_data)
print('How many unique words are in your Tfidf= ', len(set(vectorizer.get_feature_names())))