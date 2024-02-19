import random
import spacy #type: ignore
import nltk
import nltk.data
from nltk.corpus import treebank
import os
import re
nlp = spacy.load("en_core_web_sm")

# Creating stopword list:       
stopwords = spacy.lang.en.stop_words.STOP_WORDS

corpus = []
data_folder = "PMC001xxxxxx/"
filename = random.choice(os.listdir(data_folder))
file_path = os.path.join(data_folder, filename)

file = open(file_path, 'r+', encoding = "utf-8")
file = re.sub(u"[^\x01-\x7f]+",u"",file.read())


# creating tokens via nltk:
#tokens = nltk.word_tokenize(file)
#tagged = nltk.pos_tag(tokens)
#entities = nltk.chunk.ne_chunk(tagged)


# attempting to create dependency tree:
#t = treebank.parsed_sents(file)[0]
#t.draw()


introduction_doc = nlp(file)

#print(filename)
#print([token.text for token in introduction_doc])