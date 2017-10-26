import os
import markovify
import random
import json
import pickle
import configparser
import tweepy
import time

basepath = os.path.dirname(os.path.abspath(__file__))

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# Read the config file
config = configparser.ConfigParser()
config.read(basepath+'/config/config.ini')

# Set all of the variables we need for Twitter
consumer_key = config['Twitter']['consumer_key']
consumer_secret = config['Twitter']['consumer_secret']
access_token = config['Twitter']['access_token']
access_token_secret = config['Twitter']['access_token_secret']

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object to use
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


characters = ['ZACH', 'TAYLOR', 'SOOKIE', 'RORY', 'RICHARD', 'PARIS', 'MISS PATTY', \
    'MICHEL', 'MAX', 'LUKE', 'LORELAI', 'LOGAN', 'LANE', 'KIRK', 'JESS', 'JASON', \
    'JACKSON', 'EMILY', 'DEAN', 'CHRISTOPHER']

while True:
	tweet = ''
	go = True
	while go:
		for i in range(1,3):
			choice = random.choice(characters)

			with open(basepath+'/text/{}-markov-model.pickle'.format(choice), 'rb') as handle:
			    model = pickle.load(handle)

			line = choice+': '+model.make_short_sentence(70)

			if i==1:
				tweet += line+'\n'
			else:
				tweet += line

			if len(tweet) > 140:
				tweet = ''
			else:
				go = False

	api.update_status(tweet)
	time.sleep(21600)