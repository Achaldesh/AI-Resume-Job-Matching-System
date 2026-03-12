
# AI-Based Resume–Job Matching System

##  Project Overview
The AI-Based Resume–Job Matching System is a Natural Language Processing (NLP) project that automatically compares resumes with job descriptions and calculates a matching score. The system helps identify the most relevant resumes for a given job role.

This project uses TF-IDF vectorization and cosine similarity to measure the similarity between resume text and job description text.

---

##  Features
- Resume and job description comparison
- NLP-based text preprocessing
- TF-IDF vectorization
- Cosine similarity scoring
- Resume ranking based on match score
- Simple web interface using Flask

---

##  Core Concepts Used
- Natural Language Processing (NLP)
- TF-IDF (Term Frequency–Inverse Document Frequency)
- Cosine Similarity
- Text Preprocessing (Tokenization, Lemmatization)
- Resume Matching Algorithm

---

##  Tech Stack
- Python
- Flask
- spaCy
- Scikit-learn
- HTML

---

##  Project Structure
resume_job_matcher
│
├── app.py
├── matcher.py
├── requirements.txt
├── .gitignore
│
├── templates
│ └── index.html
│
├── resumes
│ ├── resume1.txt
│ └── resume2.txt
│
└── jobs



---

##  Installation

Clone the repository


git clone https://github.com/Achaldesh/AI-Resume-Job-Matching-System.git


Go to project folder


cd AI-Resume-Job-Matching-System


Install dependencies


pip install -r requirements.txt


Download spaCy language model


python -m spacy download en_core_web_sm


---

##  Run the Project

Run the Flask application


python app.py


Open browser


http://127.0.0.1:5000


Enter a job description and the system will calculate the matching score for resumes.

---

## Example Output

Job Description:

Looking for a Python developer with machine learning and data analysis skills


Output:

Resume 1 Score: 0.78
Resume 2 Score: 0.15


The resume with the highest score is the best match for the job description.

---

## Engineering Value
This project demonstrates:

- NLP pipeline development
- Resume text processing
- Vectorization techniques
- Similarity-based ranking
- Web integration using Flask

---

## Author

GitHub Profile  
https://github.com/Achaldesh

---

## License
This project is created for educational and learning purposes.
README kaise add kare

