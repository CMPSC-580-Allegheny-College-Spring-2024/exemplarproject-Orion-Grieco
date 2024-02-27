import spacy #type: ignore
import os
import pubmed_parser
from pubmed_parser import parse_pubmed_caption
import pandas as pd
from glob import glob
from bs4 import BeautifulSoup as beau
nlp = spacy.load("en_core_web_sm")

# Creating stopword list:       
stopwords = spacy.lang.en.stop_words.STOP_WORDS

data_folder = "PMC001xxxxxx/"
comparison_text = input("Enter text to compare to the article: ")
"""
for word in comparison_text.split():
    print(word)
"""

summative_dict = {}
for filename in os.scandir(data_folder):
    #print(filename)
    #file_path = os.path.join(data_folder, filename)

    open_file = open(filename.path, 'r+', encoding = "utf-8")
    prep_file = open_file.read()

    pmid_soup = beau(prep_file,'lxml')
    pmid_val = pubmed_parser.parse_pubmed_caption(prep_file)
    # removing stop words
    filtered_text = " ".join([word for word in prep_file.split() if word not in stopwords])

    soup = beau(filtered_text, "html.parser")
    for data in soup(['style', 'script']):
            data.decompose()
    text = soup.get_text()
    

    #print(f"File Name and Path : {filename} : {text} + \n")
    
    comparing_text_doc = nlp(comparison_text)
    base_doc = nlp(text)
    for dict_obj in pmid_val:
    # Creating a dictionary for the similarity matrix
        similarity_matrix = dict(INPUT= comparison_text,
        ARTICLE= {filename},
        PMID= dict_obj["pmid"],
        SIM_SCORE = base_doc.similarity(comparing_text_doc))
        
        
        
        summative_dict.update(similarity_matrix)
    #print(comparison_text, "<->", filename, base_doc.similarity(comparing_text_doc))
with(open("sim_matrix_results.json", "a+")) as file:
        file.write(f"{summative_dict}")
