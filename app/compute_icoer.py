from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_entropy(tokens):
    from collections import Counter
    from math import log2
    freqs = Counter(tokens)
    total = len(tokens)
    probs = [f / total for f in freqs.values()]
    return -sum(p * log2(p) for p in probs if p > 0)

def compute_icoer(texts):
    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(texts)
    sim_matrix = cosine_similarity(X)
    avg_similarity = np.mean(sim_matrix[np.triu_indices(len(texts), 1)])
    entropies = [compute_entropy(t.split()) for t in texts]
    avg_entropy = np.mean(entropies)
    return {
        "coerencia_lexico_semantica": round(avg_similarity, 3),
        "entropia_textual_media": round(avg_entropy, 3),
        "icoer_v7_simplificado": round((avg_similarity + (1 / (1 + avg_entropy))) / 2, 3)
    }
