import random
import spacy #type: ignore
import gensim
from gensim import corpora
import os
nlp = spacy.load("en_core_web_sm")

# Creating stopword list:       
stopwords = spacy.lang.en.stop_words.STOP_WORDS


corpus = []
data_folder = "PMC001xxxxxx/"
filename = random.choice(os.listdir(data_folder))
file_path = os.path.join(data_folder, filename)

file = open(file_path, 'r', encoding = "utf-8")
file_read_obj = file.read()
introduction_doc = nlp(file_read_obj)

#print(filename)
#print([token.text for token in introduction_doc])