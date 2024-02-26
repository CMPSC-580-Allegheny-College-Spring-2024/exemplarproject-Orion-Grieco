import random
import spacy #type: ignore
import nltk
import nltk.data
from nltk.corpus import treebank
import os
import re
import pandas as pd
from glob import glob
from bs4 import BeautifulSoup as beau
nlp = spacy.load("en_core_web_sm")

# Creating stopword list:       
stopwords = spacy.lang.en.stop_words.STOP_WORDS

data_folder = "PMC001xxxxxx/"
comparison_text = input("Enter text to compare to the article: ")


for filename in os.scandir(data_folder):
    #print(filename)
    #file_path = os.path.join(data_folder, filename)

    open_file = open(filename.path, 'r+', encoding = "utf-8")
    open_file = re.sub(u"[^\x01-\x7f]+",u"",open_file.read())

    pmid_soup = beau(open_file,'lxml')
    pmid_val = pmid_soup.find('pub-id', attrs={'pub-id-type': 'pmid'}).text

    # removing stop words
    filtered_text = " ".join([word for word in open_file.split() if word not in stopwords])

    soup = beau(filtered_text, "html.parser")
    for data in soup(['style', 'script']):
            data.decompose()
    text = soup.get_text()
    

    #print(f"File Name and Path : {filename} : {text} + \n")
    
    comparing_text_doc = nlp(comparison_text)
    base_doc = nlp(text)
    
    # Creating a dictionary for the similarity matrix
    similarity_matrix = dict({f"User Input: {comparison_text} + ARTICLE: {filename} + PMID :{pmid_val}": base_doc.similarity(comparing_text_doc)})
    
    with(open("sim_matrix_results.txt", "a+")) as file:
        file.write(f"{similarity_matrix}" + "\n")
    #print(comparison_text, "<->", filename, base_doc.similarity(comparing_text_doc))



