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

data_folder = "/Mouseion/PMC001xxxxxx"
comparison_text = input("Enter text to compare to the article: ")
"""
for word in comparison_text.split():
    print(word)
"""
all_found = 0
partly_found = 0
summative_dict = {}
for filename in os.scandir(data_folder):
    #print(filename)
    #file_path = os.path.join(data_folder, filename)

    open_file = open(filename.path, 'r+', encoding = "utf-8")
    prep_file = open_file.read()

    pmid_soup = beau(prep_file,'lxml')
    try:
        pmid_val = pubmed_parser.parse_pubmed_caption(prep_file)
    except:
        pmid_val = "Nan"
    # removing stop words
    filtered_text = " ".join([word for word in prep_file.split() if word not in stopwords])

    soup = beau(filtered_text, "html.parser")
    for data in soup(['style', 'script']):
            data.decompose()
    text = soup.get_text()
    valid_counter = 0
    invalid_counter = 0

    comparing_text_doc = nlp(comparison_text)
    base_doc = nlp(text)
    for word in comparison_text.split():
        if sum(word in text) == 2:
            partly_found += 1
            if type(pmid_val) == list:
                valid_counter += 1
                for dict_obj in pmid_val:
            # Creating a dictionary for the similarity matrix
                    temp_matrix = dict(INPUT= comparison_text,
                    PMID= dict_obj["pmid"],
                    SIM_SCORE = base_doc.similarity(comparing_text_doc),
                    INTEGRITY = "VALID")
                    with(open("sim_matrix_results.json", "a+")) as file:
                        file.write(f"{temp_matrix}"+ "\n")
        else:
            invalid_counter += 1
            temp_matrix = dict(INPUT= comparison_text,
            PMID = float("Nan"), 
            SIM_SCORE = base_doc.similarity(comparing_text_doc),
            INTEGRITY = "INVALID")
            with(open("sim_matrix_results.json", "a+")) as file:
                file.write(f"{temp_matrix}"+"\n")
        
        if sum(word in text) == len(comparison_text.split()):
            all_found += 1
            if type(pmid_val) == list:
                valid_counter += 1
                for dict_obj in pmid_val:
            # Creating a dictionary for the similarity matrix
                    temp_matrix = dict(INPUT= comparison_text,
                    PMID= dict_obj["pmid"],
                    SIM_SCORE = base_doc.similarity(comparing_text_doc),
                    INTEGRITY = "VALID")
                    with(open("sim_matrix_results.json", "a+")) as file:
                        file.write(f"{temp_matrix}"+ "\n")
            else:
                invalid_counter += 1
                temp_matrix = dict(INPUT= comparison_text,
                PMID = float("Nan"), 
                SIM_SCORE = base_doc.similarity(comparing_text_doc),
                INTEGRITY = "INVALID")
                with(open("sim_matrix_results.json", "a+")) as file:
                    file.write(f"{temp_matrix}"+"\n")
    #print(comparison_text, "<->", filename, base_doc.similarity(comparing_text_doc))
print("Articles with all words found: ", all_found, "\n", "Articles with two words found: ", partly_found, "\n")
print(f"Out of all of the articles assessed, only {(sum(valid_counter+invalid_counter)/100)*invalid_counter}% were deemed invalid by the algorithm")

