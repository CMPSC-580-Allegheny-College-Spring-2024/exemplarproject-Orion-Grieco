[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)

# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

This repository contains student project materials, including project report, data, code, and references to literature for this departmentally-sponsored project. __As you complete each of the below sections in this document, please be sure to remove the preamble text so that it does not appear in your work.__ Please work with your first reader to answer any questions or concerns that you may have.

## GitHub Handle: Orion-Grieco

## Name: Orion Grieco

## Major: DS

## Project Name: Mouseion

Here, think of an interesting name of the work that bring a freshness and excitement to the area of this project. Consider using a name that carries some information about what the project and provides some hint at what the project does without being too wordy.

---

## Overview

- The project itself (Mouseion) works as a fact-checker to compare user-inputted text entries to a corpus of varying documents. The program itself works by first iterating through a corpus of several documents. As the AI model iterates through each document, it estimates a value based off of a similarity matrix that compares the content of the article and the user-inputted entry(ies), and returns the aforementioned similarity matrix value. This value serves as a score of how verifiable the input is relative to the content of the article. The end result of the program is that it will return the PMID value and similarity matrix value of each article within the corpus. The results will also be contained within a JSON file. The machine learning model will also prune duplicate values, as it is converted into a set before it is written into the JSON file container, thus effectively removing any duplicate values thay may persist through parsing the initial articles or corresponding files.
- The main hypothesis of this project is that the AI model can predict similarity matrix scores with some accuracy, but may be subject to an inherent bias, or is at least not as accurate as initially presumed.
- The significance of this project serves to test AI, machine learning, and the aspect of fact-checking. As it stands, the age of misinformation is well and alive, and this serves as a proof-of-concept to combat this issue. Using AI and machine learning, we can work towards a means of accurately determining or interpreting data and articles through something as simple as a few keywords.

## Literature Review

TODO: Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further contributes to the `why is the project important?` question. The number of scholarly work included in the literature review may vary depending on the project.

## Methods

TODO: Discuss the methods of the project to be able to answer the `how` question (`how was this project completed?`). The methods section in an academic research outlines the specific procedures, techniques, and methodologies employed to conduct the study, offering a transparent and replicable framework for the research. It details the resources behind the work, in terms of, for example, the design of the algorithm and the experiment(s), data collection methods, applied software libraries, required tools, the types of statistical analyses and models which are applied to ensure the rigor and validity of the study. This section provides clarity for other researchers to understand and potentially replicate the study, contributing to the overall reliability and credibility of the research findings.

* The project went through several iterations, utilizing a mix of the NLP models Gensim, NLTK, and SpaCy. I believe I went through about 6 different versions before I arrived at the current one, which utilizes SpaCy, Beautiful Soup (BS4), and Pubmed Parser.
* The current iteration functions as the following in the steps ordered:
  * The user inputs a series of strings to compare to relative to the articles in the corpus of documents.
  * The NLP model then begings to iteratively parse through each article within the corpus.
  * The NLP model will pull the PubMed ID numer of the article it is parsing through.
  * The NLP model estimates a simlarity matrix score based on the user input's accuracy relative to the content of the article it parses through.
  * The program will then take these two results obtained by the NLP, as well as the user fed input, and create a dictionary object of these three attributes for each of the articles within the corpus.
  * The data is then stored within a JSON file.
* Over all the iterations, the shared functionality was an automated system via an NLP model that would parse through each article in an established corpus, and calculate a similarity matrix score relative to the user input as it was determined to be found in the article. The introduction of parsing the article to find its respective PubMed ID brought along the use of SpaCy, as it seemed the majority of Gensim APIs I had found were all outdated or deprecated, despite being less than a year old at most

## Using the Artifact

TODO: The result of your work will be the delivery of some type of artifact which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). To allow the user to experience and execute your artifact, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.

## Results and Outcomes

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)
