# Phishing Website Detection System

## Project Overview
This project uses Machine Learning (Random Forest algorithm) to detect phishing websites with 98.5% accuracy. Phishing is a cyber attack where hackers create fake websites that look like real ones (banking, social media, email) to steal user passwords, credit card numbers, and personal information.

This system analyzes website characteristics and automatically identifies whether a website is legitimate or a phishing scam.

## How Phishing Detection Works
The system examines 48 different features of a website including:
- URL length (phishing sites use very long URLs)
- Number of dots and dashes in the URL
- Domain age (phishing domains are often newly registered)
- Presence of HTTPS (secure connection)
- Special characters like @, ~, _, %
- Number of subdomains
- Form action patterns
- External resource links

## Results
The Random Forest model achieves excellent performance:

| Metric | Score | Meaning |
|--------|-------|---------|
| Accuracy | 98.44% | Overall correctness of predictions |
| Precision | 98.43% | When system says "phishing", it's right 98.43% of the time |
| Recall | 98.51% | System catches 98.51% of actual phishing websites |

## Technologies Used
- **Python 3.x** - Programming language
- **pandas** - Data loading and manipulation
- **numpy** - Numerical computations
- **scikit-learn** - Machine Learning (Random Forest algorithm)
- **matplotlib** - Data visualization

## How to Run the Project

### Step 1: Install Python
Download and install Python 3.8 or higher from [python.org](https://python.org)

### Step 2: Download the Dataset
Download the phishing dataset from Kaggle:
[https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning](https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning)

Save the file `Phishing_Legitimate_full.csv` in the same folder as the Python script.

### Step 3: Install Required Packages
Open terminal (command prompt) and run:
```bash
pip install pandas numpy scikit-learn matplotlib