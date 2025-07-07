import re
import spacy
from app.config import ICOER_CONFIG

nlp = spacy.load("pt_core_news_sm")

def clean_and_tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    doc = nlp(text)
    tokens = [
        token.lemma_ for token in doc
        if not token.is_stop and len(token) >= ICOER_CONFIG['min_token_length']
    ]
    return tokens
