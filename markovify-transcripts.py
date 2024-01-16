import os
import markovify
import nltk
import re
import json
import pickle

nltk.download('averaged_perceptron_tagger')

basepath = os.path.dirname(os.path.abspath(__file__))

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

characters = ['ZACH', 'TAYLOR', 'SOOKIE', 'RORY', 'RICHARD', 'PARIS', 'MISS PATTY', \
    'MICHEL', 'MAX', 'LUKE', 'LORELAI', 'LOGAN', 'LANE', 'KIRK', 'JESS', 'JASON', \
    'JACKSON', 'EMILY', 'DEAN', 'CHRISTOPHER', 'all-lines']

# loop through files
for c in characters:
    with open(basepath+'/text/{}.txt'.format(c)) as f:
        lines = f.read()

    model = POSifiedText(lines)

    with open(basepath+'/text/{}-markov-model.pickle'.format(c), 'wb') as handle:
        pickle.dump(model, handle)

    print('{} done'.format(c))