import spacy  # type: ignore
import os
import pubmed_parser
import pandas as pd
from glob import glob
from bs4 import BeautifulSoup as beau

nlp = spacy.load("en_core_web_sm")

# Creating stopword list:
stopwords = spacy.lang.en.stop_words.STOP_WORDS

data_folder = "data/PMC001xxxxxx"
comparison_text = input("Enter text to compare to the article: ")
"""
for word in comparison_text.split():
    print(word)
"""
wiped_file = open("sim_matrix_results.json", "w")
wiped_file.truncate()
wiped_file.close()
temp_dict = {}
data_list = []
summative_score = 0
for filename in os.scandir(data_folder):

    open_file = open(filename.path, "r+", encoding="utf-8")
    prep_file = open_file.read()

    pmid_soup = beau(prep_file, "lxml")

    try:
        pmid_val = pubmed_parser.parse_pubmed_caption(prep_file)
    except:
        pass
    # removing stop wordsa
    filtered_text = " ".join(
        [word for word in prep_file.split() if word not in stopwords]
    )

    soup = beau(filtered_text, "html.parser")
    for data in soup(["style", "script"]):
        data.decompose()
    text = soup.get_text()

    comparing_text_doc = nlp(comparison_text)
    base_doc = nlp(text)

        # Creating a dictionary for the similarity matrix
    temp_dict = {
        "INPUT": comparison_text,
        "PMID": pmid_val[0]["pmid"], #type: ignore
        "SIM_SCORE": base_doc.similarity(comparing_text_doc),
    }
    summative_score += float(temp_dict["SIM_SCORE"])
    data_list.append(temp_dict)
    with open("sim_matrix_results.json", "a+") as file:
        file.write(f"{data_list}" + "\n")

    # print(data_list, "@")


# print(comparison_text, "<->", filename, base_doc.similarity(comparing_text_doc))
