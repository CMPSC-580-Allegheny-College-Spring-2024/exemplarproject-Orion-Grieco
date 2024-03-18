[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)

# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

This repository contains student project materials, including project report, data, code, and references to literature for this departmentally-sponsored project. __As you complete each of the below sections in this document, please be sure to remove the preamble text so that it does not appear in your work.__ Please work with your first reader to answer any questions or concerns that you may have.

## GitHub Handle: Orion-Grieco

## Name: Orion Grieco

## Major: DS (Data Science)

## Project Name: Mouseion

## Overview

- The project itself (Mouseion) works as a fact-checker to compare user-inputted text entries to a corpus of varying documents. The program itself works by first iterating through a corpus of several documents. As the AI model iterates through each document, it estimates a value based off of a similarity matrix that compares the content of the article and the user-inputted entry(ies), and returns the aforementioned similarity matrix value. This value serves as a score of how verifiable the input is relative to the content of the article. The end result of the program is that it will return the PMID value and similarity matrix value of each article within the corpus. The results will also be contained within a JSON file. The machine learning model will also prune duplicate values, as it is converted into a set before it is written into the JSON file container, thus effectively removing any duplicate values thay may persist through parsing the initial articles or corresponding files.
- The main hypothesis of this project is that the AI model can predict similarity matrix scores with some accuracy, but may be subject to an inherent bias, or is at least not as accurate as initially presumed.
- The significance of this project serves to test AI, machine learning, and the aspect of fact-checking. As it stands, the age of misinformation is well and alive, and this serves as a proof-of-concept to combat this issue. Using AI and machine learning, we can work towards a means of accurately determining or interpreting data and articles through something as simple as a few keywords.

## Literature Review

TODO: Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further contributes to the `why is the project important?` question. The number of scholarly work included in the literature review may vary depending on the project.

## Methods

### Method Overview

* The project went through several iterations, utilizing a mix of the NLP models Gensim, NLTK, and SpaCy. I believe I went through about 6 different versions before I arrived at the current one, which utilizes SpaCy, Beautiful Soup (BS4), and Pubmed Parser.
* Across all the iterations, the shared functionality was an automated system via an NLP model that would parse through each article in an established corpus, and calculate a similarity matrix score relative to the user input as it was determined to be found in the article. The introduction of parsing the article to find its respective PubMed ID brought along the use of SpaCy, as it seemed the majority of Gensim APIs I had found were all outdated or deprecated, despite being less than a year old at most.

### Algorithm Design

* The current iteration functions as the following in the steps ordered:

  * The user inputs a series of strings to compare to relative to the articles in the corpus of documents.
  * The NLP model then begings to iteratively parse through each article within the corpus.
  * The NLP model will pull the PubMed ID numer of the article it is parsing through.
  * BeautifulSoup it then used to strip the articles of all extraneous HTML and XML tags and characters. This newly stripped document is what it used in calcuating the similarity matrix score.
  * The NLP model estimates a simlarity matrix score based on the user input's accuracy relative to the content of the article it parses through.
  * The program will then take these two results obtained by the NLP, as well as the user fed input, and create a dictionary object of these three attributes for each of the articles within the corpus.
  * The data is then stored within a JSON file.

### Required Tools

* Pubmed Parser library (can be downloaded from the PubMed API)
* SpaCy NLP Model
* Beautiful Soup

### Applied Software Libraries

* Python default `os` library

### Analysis

* The algorithm utilizes a similarity matrix, in conjunction with word vectors and/or context-sensitive tensors. There are two models utilized within SpaCy in regard to word similarity/similarity matrices. The `en_core_web_sm` model utilizes tensors, while the `en_core_web_sm` model utilizes 1 million+ word vectors.
* The similarity matrix score is a calculated value to represent the similarity between two inputs, in this case being the user-provided input and the article being evaluated. This score is being leveraged as a means to establish a user-digestable format of the accuracy of an article relative to the user input (how related the article is to the user-provided input on a scale of 0-1).

## Using the Artifact

* The user will first cd into the directory `Mouseion/src.`
* The user will then run the program via the terminal command `python main.py` or `python3 main.py` depending on their OS or Python version.
* The user will be prompted to provide an input, which can consist of a direct phrase, or one or multiple keywords.
* Once the user has provided an input and hit `Enter` or `Return` on their keyboard, the artifact will then begin to run based on the provided input of a phrase or keywords, and begin to calculate similarity matrix scores on each article with in the corpus relative to the user-provided input, as well as search for the PMID of each article for reference within the PubMed databse.
* The results are stored within the `sim_matrix_results.json` file, with each entry of data corresponding to an article within the corpus. Again, each entry consists of a dictionary containing the user input, the PMID of the article, and the similarity matrix score of each article.

## Results and Outcomes

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

### End Result of Project

* Overall, the project was somewhat tedious, in terms of finding a viable format to create this project. The majority of Gensim was unreliable, as I was regularly finding out that the code I was working with utilized deprecated functions, that were replaced with less wieldy umbrella functions to take the place of multiple methods in some cases. This was even in spite of the tutorials I had followed being less than a year old, with seemingly large portions of the Gensim structure no longer being viable or usable as a whole.
* The current function of the project is suitable for its intended purpose, though there can be improivements in the NLP and machine learning aspects of the artifact.

### Proposed Enhancements

* An initial thought of improving the artifact would be to utilize a more versatile machine learning or NLP model that can determine more between the user input and article(s) rather than a direct correlation based upon a relative similarity.
  * An ideal enhancement for this idea would to be to search for either a phrase (or a string within an article that matches the user-inputted phrase as close as possible), or a set of keywords.
  * Another enhancement in kind to this general notion would be to utilize a larger or more robust model as well to further support the accuracy of the similarity matrix scores, as well as improve the overall accuracy and general function of the model.
* General research into interactions between models as well would be convenient, as to look for different ways to enhance the function of the artifact through "mixing and matching" of a multitude of packages, modules, or models altogether.

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)
