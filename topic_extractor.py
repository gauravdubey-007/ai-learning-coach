import nltk
from pdf_reader import extract_text

# Pehli baar download karo
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag

def extract_topics(text):
    # Words nikalo
    words = word_tokenize(text)
    
    # Stop words hatao (is, the, a, etc.)
    stop_words = set(stopwords.words('english'))
    
    # POS tagging - important words dhundo
    tagged = pos_tag(words)
    
    topics = []
    for word, tag in tagged:
        # Sirf Nouns lo (NN = noun)
        if tag in ['NN', 'NNP', 'NNS'] and word.lower() not in stop_words:
            if len(word) > 2:
                topics.append(word)
    
    # Duplicate hatao
    topics = list(set(topics))
    return topics

# Test
text = extract_text("notes.txt")
topics = extract_topics(text)

print("✅ Topics mile:")
for i, topic in enumerate(topics):
    print(f"{i+1}. {topic}")