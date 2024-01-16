import os
import markovify
import random
import pickle
import tweepy
import time
import re
from local_settings import *

basepath = os.path.dirname(os.path.abspath(__file__))

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# Set all of the variables we need for Twitter
consumer_key = os.environ.get('X_CONSUMER_KEY')
consumer_secret = os.environ.get('X_CONSUMER_SECRET')
access_token = os.environ.get('X_ACCESS_TOKEN_KEY')
access_token_secret = os.environ.get('X_ACCESS_TOKEN_SECRET')

# Authenticate with Twitter
# Create an API object to use
api = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=True)

characters = ['ZACH', 'TAYLOR', 'SOOKIE', 'RORY', 'RICHARD', 'PARIS', 'MISS PATTY', \
    'MICHEL', 'MAX', 'LUKE', 'LORELAI', 'LOGAN', 'LANE', 'KIRK', 'JESS', 'JASON', \
    'JACKSON', 'EMILY', 'DEAN', 'CHRISTOPHER']

def post_tweet():
	tweet = ''
	r = random.randint(1,101)
	if r < 51:
		go = True
		while go:
			for i in range(1,3):
				choice = random.choice(characters)

				with open(basepath+'/text/all-lines-markov-model.pickle', 'rb') as handle:
						model = pickle.load(handle)
						
				line = choice+': '+model.make_short_sentence(140)

				if i==1:
					tweet += line+'\n'
				else:
					tweet += line

				if len(tweet) > 280:
					tweet = ''
				else:
					go = False
	else:
		choice = random.choice(characters)

		with open(basepath+'/text/all-lines-markov-model.pickle', 'rb') as handle:
			model = pickle.load(handle)

		tweet = choice+': '+model.make_short_sentence(280)

	print(tweet)
	api.create_tweet(text = tweet)
	time.sleep(3600)

while True:
	post_tweet()