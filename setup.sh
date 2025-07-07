#!/bin/bash

echo "🚀 Iniciando configuração do ambiente ICOER..."

# Criação de ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Upgrade do pip e instalação de dependências
pip install --upgrade pip
pip install -r requirements.txt

# Download do modelo SpaCy para português
python -m spacy download pt_core_news_sm

echo "✅ Ambiente pronto. Ative com: source .venv/bin/activate"
