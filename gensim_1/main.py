import gensim
from pprint import pprint
from gensim import corpora
from smart_open import smart_open
from gensim.utils import simple_preprocess
import os
import random


# Choosing a random file and returning a summary
corpus = []
data_folder = "PMC001xxxxxx/"
filname = random.choice(os.listdir(data_folder))
file_path = os.path.join(data_folder, filname)

text = "".join(line for line in smart_open(file_path, encoding = "utf-8"))
pprint(summarize(text, word_count = 100))
print("\n")
print(keywords(text, words = 100))
with open(file_path, "r+") as f:
        termsim_matrix = inner_product.InnerProductSimilarity(f)
        