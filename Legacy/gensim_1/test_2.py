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

# Creating and a numeric corpus
with open("numeric_corpus.txt", "w+") as num_corpus:
        num_corpus.write(str(corpus))
        
        
# Creating a corpus of keywords
with open("textual_corpus.txt", "w+") as key_corpus:
        for filename in os.listdir(data_folder):    
                with open(data_folder + filename, "r+") as key_doc:
                        for line in key_doc:
                                preppedtext = key_doc.read()
                                dictionary = corpora.Dictionary(simple_preprocess(preppedtext, deacc = True))
        key_corpus.write(dictionary.token2id)
        
        
        
# I forgot what this does
data_folder = "PMC001xxxxxx/"
for filename in os.listdir(data_folder):
        with open(data_folder + filename, "r+") as f:
                sub_doc = f.read()
                tokens = [simple_preprocess(sub_doc)]
                data_dictionary = corpora.Dictionary()
                corpus = [data_dictionary.doc2bow(doc, allow_update = True) for doc in tokens]
                model = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word = data_dictionary, num_topics = 5)
                pprint(model.print_topics(num_words = 10))