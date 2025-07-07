import pytest
from app.compute_icoer import compute_icoer

def test_compute_icoer_basic():
    texts = [
        "o brasil é um país tropical",
        "o brasil é um país tropical",
        "o brasil é um país tropical"
    ]
    results = compute_icoer(texts)
    assert 'icoer_v7_simplificado' in results
    assert 0.0 <= results['icoer_v7_simplificado'] <= 1.0
