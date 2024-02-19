import gensim
import nltk
import nltk.data
from pprint import pprint
from gensim import corpora
from smart_open import smart_open
from gensim.utils import simple_preprocess
import os
import re
import random
import heapq
import bs4 as bs
import urllib.request
# Choosing a random file and returning a summary
corpus = []
data_folder = "PMC001xxxxxx/"
filname = random.choice(os.listdir(data_folder))
file_path = os.path.join(data_folder, filname)

text = "".join(line for line in smart_open(file_path, encoding = "utf-8"))


preppedtext = open(file_path,"r+")
article = preppedtext.read()
parsed_article = bs.BeautifulSoup(article, "lxml")
paragraphs = parsed_article.find_all("p")
article_text = ""

for p in paragraphs:
        article_text += p.text
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
        sentence_list = nltk.sent_tokenize(article_text)
        stopwords = set(nltk.corpus.stopwords.words('english'))
        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
                if word not in stopwords:
                        if word not in word_frequencies.keys():
                                word_frequencies[word] = 1
                        else:
                                word_frequencies[word] += 1
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
                word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
                sentence_scores = {}
                for sent in sentence_list:
                        for word in nltk.word_tokenize(sent.lower()):
                                if word in word_frequencies.keys():
                                        if len(sent.split(' ')) < 30:
                                                if sent not in sentence_scores.keys():
                                                        sentence_scores[sent] = word_frequencies[word]
                                                else:
                                                        sentence_scores[sent] += word_frequencies[word]
                summary_sentences = heapq.nlargest(7, sentence_scores, key = sentence_scores.get)                             
                summary = ' '.join(summary_sentences)
                print(summary)