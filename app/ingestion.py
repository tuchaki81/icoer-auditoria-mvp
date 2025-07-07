import pandas as pd

def load_text_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def load_csv_column(path, column='text'):
    df = pd.read_csv(path)
    return df[column].dropna().tolist()
