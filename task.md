1 Problem Statement
Design and implement a retrieval-based FAQ chatbot capable of answering user questions in a specific domain
using Natural Language Processing techniques.
The chatbot should:
• accept a natural language query from the user
• identify the most semantically similar question from a predefined FAQ dataset
• return the corresponding answer
1.1 Possible Domains
• university admissions
• healthcare FAQs
• software support
• banking
• restaurants
• travel
• sports
• gaming
• programming tutorials
• e-commerce
• or any other approved domain
2 Learning Objectives
After completing this assignment, you must be able to:
• preprocess textual data
• represent text using embeddings/vector representations
• compute semantic similarity
• build a retrieval-based conversational system
• evaluate chatbot performance
• analyze strengths and weaknesses of NLP systems
• use modern Python NLP libraries effectively
3 Functional Requirements
3.1 FAQ Dataset
Create or collect an FAQ dataset containing at least 50 question-answer pairs. The dataset may be manually
created, collected from websites, or adapted from public resources. Please store your dataset in CSV, JSON, or
Excel format.
3.2 User Query Processing
The chatbot should accept user input, preprocess the text, and compare it with stored FAQ questions.
1
3.3 Similarity-Based Retrieval
The chatbot must retrieve the most relevant FAQ question, and return its answer. You must use at least one of
the following approaches:
• TF-IDF + cosine similarity
• sentence embeddings
• transformer embeddings
3.4 Confidence Handling
Your chatbot should include a confidence mechanism. For example, if similarity score is below a threshold, it
should return a fallback response such as “Sorry, I could not find a reliable answer.”
3.5 Evaluation
You must evaluate the chatbot on at least 15–20 test queries. You should include successful examples, failure
cases, and analysis.
4 Technical Requirements
4.1 Programming Language
Python
4.2 Suggested Libraries
• NLTK
• spaCy
• scikit-learn
• sentence-transformers
• Transformers
• pandas
5 Suggested Development Workflow
You are encouraged to follow these steps.
5.1 Step 1: Select Domain
Choose a domain with sufficient FAQ data. E.g., NED University admissions, Airline customer support, Online
shopping FAQs, Hospital information desk, etc.
5.2 Step 2: Build Dataset
Create a structured dataset.
5.3 Step 3: Text Preprocessing
Preprocessing may include lowercasing, punctuation removal, tokenization, stopword removal, lemmatization, etc.
2
5.4 Step 4: Text Representation
• Option A: TF-IDF
Represent FAQ questions using TF-IDF vectors.
• Option B: Sentence Embeddings
Use pretrained embedding models such as all-MiniLM-L6-v2.
5.5 Step 5: Similarity Computation
You may use cosine similarity, Euclidean distance, or any another appropriate metric.
5.6 Step 6: Response Generation
Your system should return the best matching answer, similarity score, and optionally, matched FAQ question.
5.7 Step 7: Evaluation
Test your chatbot with paraphrased queries, incomplete queries, spelling mistakes, and ambiguous questions.
6 Minimum Expected Features
A satisfactory submission should include:
• working chatbot
• FAQ dataset
• semantic matching
• confidence threshold
• evaluation examples
• short report
7 Important Academic Guidelines
You are expected to write your own code, clearly cite external resources, mention any pretrained models used,
and explain all borrowed code snippets.
Use of AI tools is allowed only if they are properly acknowledged, and fully understood.
8 Deliverables
• Source Code
properly commented Python code.
• Dataset
FAQ dataset file.
• Short Report (PDF)
approximately 10 pages.
• Demonstration
Recorded demonstration.
3
9 Report Template
9.1 Title Page
• Assignment title
• Names and Roll nos of group members (max 2)
9.2 Introduction
Briefly describe the chatbot objective, the selected domain, and the motivation.
9.3 Dataset Description
Please include dataset source, number of FAQs, and sample entries.
9.4 Methodology
9.4.1 Preprocessing
E.g., tokenization, stopword removal, etc.
9.4.2 Text Representation
TF-IDF, embeddings, transformer model used.
9.4.3 Similarity Computation
9.5 Implementation
Describe libraries used, system architecture, and important functions/modules.
9.6 Experimental Results
Please include test queries, chatbot responses, and similarity scores.
9.7 Error Analysis and Discussion
Please discuss incorrect responses, ambiguous queries, and limitations. This section is extremely important. You
must reflect on the semantic limitations, dataset quality, paraphrasing issues, spelling errors, and computational
constraints.
9.8 Conclusion
Please summarize achievements, lessons learned, and possible improvements.
9.9 References
Please list libraries, tutorials, datasets, research papers, and websites used. Please use IEEE citation style