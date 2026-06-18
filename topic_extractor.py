import nltk
import os

# Streamlit Cloud ke liye NLTK data download
nltk.data.path.append('/home/appuser/nltk_data')

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
nltk.download('stopwords', quiet=True)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

def extract_topics(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tagged = pos_tag(words)
    
    topics = []
    for word, tag in tagged:
        if tag in ['NN', 'NNP', 'NNS'] and word.lower() not in stop_words:
            if len(word) > 2:
                topics.append(word)
    
    topics = list(set(topics))
    return topics
