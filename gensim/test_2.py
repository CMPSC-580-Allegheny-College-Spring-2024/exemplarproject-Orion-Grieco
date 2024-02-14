import gensim
from gensim import corpora
from pprint import pprint
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os

docs = open(r"oa_comm_txt.incr.2024-02-12.filelist.csv", "r+")
tokens = [simple_preprocess(sub_doc) for sub_doc in docs]
data_dictionary = corpora.Dictionary()
corpus = [data_dictionary.doc2bow(doc, allow_update = True) for doc in tokens]
pprint(corpus)