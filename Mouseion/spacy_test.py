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

'''
token_file = nlp(file)
with(open("token_pages.txt", "w+")) as myfile:
        for token in token_file:
                myfile.write(f"{token.text}, {token.has_vector}, {token.vector_norm}, {token.is_oov}" + "\n")
'''
print(f"File Name and Path : {filename} : {file}")
comparison_text = input("Enter text to compare to the article: ")
comparing_text_doc = nlp(comparison_text)
base_doc = nlp(file)
print(comparison_text, "<->", filename, base_doc.similarity(comparing_text_doc))

#print(filename)
#print([token.text for token in introduction_doc])