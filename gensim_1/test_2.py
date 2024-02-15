import gensim
from gensim import corpora
from pprint import pprint
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os
gensim_1\PMC001xxxxxx/PMC1193645.xml
# Creating a corpus
docs = open(r"gensim/data/PMC001xxxxxx/PMC1193645.xml", "r+")
tokens = [simple_preprocess(sub_doc) for sub_doc in docs]
data_dictionary = corpora.Dictionary()
corpus = [data_dictionary.doc2bow(doc, allow_update = True) for doc in tokens]
#pprint(corpus)

# Creating a dictionary from a text file
dictionary = corpora.Dictionary(simple_preprocess(line, deacc = True) for line in open(r"gensim/data/PMC001xxxxxx/PMC1193645.xml"))
print(dictionary.token2id)