import gensim
from gensim import corpora
from pprint import pprint
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os

# Creating a corpus
corpus = []
data_folder = "PMC001xxxxxx/"
for filename in os.listdir(data_folder):
        with open(data_folder + filename, "r+") as f:
                sub_doc = f.read()
                tokens = [simple_preprocess(sub_doc)]
                data_dictionary = corpora.Dictionary()
                corpus = [data_dictionary.doc2bow(doc, allow_update = True) for doc in tokens]
pprint(corpus)

# Creating a dictionary from a text file
#dictionary = corpora.Dictionary(simple_preprocess(line, deacc = True) for line in open(r"PMC001xxxxxx/PMC1193645.xml"))
#print(dictionary.token2id)