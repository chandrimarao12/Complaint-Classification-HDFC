# Complaint Classification - HDFC Bank

## Description
This project focuses on automating the classification of customer complaints for HDFC Bank using advanced Natural Language Processing (NLP) and Machine Learning techniques. The aim is to improve customer service by categorizing complaints into meaningful labels (e.g., "Fraud & Security Concerns," "Credit Card Issues," etc.), prioritizing resolutions, and enabling better operational efficiency.

The dataset for this project was obtained through web scraping from online consumer forums and complaint portals. A combination of preprocessing techniques, unsupervised learning, and supervised models were used to handle multi-label classification challenges.

## Features
- **Text Preprocessing:** Noise removal, tokenization, normalization, and feature extraction (TF-IDF).
- **Unsupervised Topic Modeling:** Latent Dirichlet Allocation (LDA) for identifying complaint categories.
- **Zero-Shot Classification:** Assigning labels to complaints without predefined categories.
- **Class Imbalance Handling:** Synthetic Minority Oversampling Technique (SMOTE).
- **Model Implementation:** Using XGBoost for multi-label classification.
- **Evaluation Metrics:** Precision, recall, F1-score, and accuracy.

## Dataset
- **Source:** Scraped from online complaint forums "https://www.consumercomplaints.in/".
- **Structure:** Textual data with metadata.
- **Preprocessing:** Cleaned and normalized textual data for effective feature extraction and classification.

### Dataset Columns:
- `complaint_link`: Heading of the original complaint.
- `description`: Raw text of the complaint.
- `cleaned_description`: Preprocessed complaint text.
- `labels`: Assigned complaint categories.
- `polarity`: Sentiment polarity of the complaint.
- `severity`: Priority level (High/Medium/Low).
- `urgency`: Urgency level (Urgent/Non-Urgent).

## Dependencies
To run this project, you need the following dependencies:
- Python 3.8+
- Libraries:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `imblearn`
  - `xgboost`
  - `nltk`
  - `spacy`
  - `beautifulsoup4`
  - `requests`
  - `matplotlib` (optional, for visualization)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/complaint-classification-hdfc.git
   cd complaint-classification-hdfc
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   (Have the dependencies required with suitable versions)
   ```

3. Download the final dataset or scrape data using the provided scripts.

## Usage
Refer to the '.ipynb' scripts provided to see how the further process has been done.



## Results
The model achieved an overall accuracy of 89%. Categories like "Fees & Penalties" and "Rewards & Cashback" performed exceptionally well. Prior to applying SMOTE, the model was biased toward majority classes, resulting in poor performance on minority categories. However, after using SMOTE to balance the dataset, the model's ability to classify complaints across all categories improved significantly.

## Future Work
- Improve classification for minority classes using advanced ensemble methods.
- Extend the system to prioritize complaints based on severity and urgency.
- Develop a user-friendly interface for real-time classification.

## Acknowledgments
- **Libraries Used:** BeautifulSoup, Scikit-learn, XGBoost, and others.
- **Data Source:** www.consumercomplaints.in
- **Tools:** Python, Jupyter Notebook, and related frameworks.

Feel free to contribute !
