# Análise de Coerência Informacional (ICOER)

Este repositório contém um notebook para análise de coerência informacional em textos, utilizando o índice ICOER.

## Como Usar

Clique no botão abaixo para abrir e executar o notebook de análise diretamente no Google Colab. Não é necessário instalar nada!

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tuchaki81/icoer-auditoria-mvp/blob/main/notebooks/icoer_text_analysis.ipynb)

### Sobre o Notebook
O notebook `icoer_text_analysis.ipynb` permite que você:
- Insira um texto com várias frases.
- Calcule o índice ICOER para cada frase.
- Exporte os resultados para um arquivo CSV.
- Visualize um gráfico com os resultados da análise.

# ICOER v7 — Auditoria Ética Automatizada de LLMs via Coerência Informacional

Este projeto implementa um MVP funcional para calcular o Índice de Coerência Informacional (**ICOER v7**) em saídas de modelos de linguagem natural (LLMs), com foco em auditoria ética automatizada, transparente e escalável.

🔎 O **ICOER** é uma métrica vetorial projetada para quantificar a coerência semântica, léxica, estrutural e afetiva das saídas de modelos de linguagem, servindo como indicador de confiabilidade e integridade textual.

---

## 📁 Estrutura

- `app/` — Módulos principais de processamento e cálculo (pipeline, ingestão, relatórios).
- `data/raw/` — Dados de entrada para auditoria.
- `notebooks/` — Execução interativa via Jupyter.
- `tests/` — Testes unitários com `pytest`.
- `streamlit_app.py` — Interface interativa baseada em Streamlit (experimento opcional).
- `workflows/` — Arquivos para integração com CI/CD (ex: GitHub Actions).

---

## 📦 Requisitos

Instale com:

```bash
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
```

---

## 🚀 Execução

1. Prepare um arquivo `.csv` com uma coluna chamada `text`.
2. Execute o notebook:

```bash
jupyter notebook notebooks/notebook_icoer_mvp.ipynb
```

3. Gere automaticamente um relatório com as métricas de coerência.
4. Execute os testes para validar o funcionamento:

```bash
pytest
```

---

## ⚡ Demonstração Rápida

```bash
# Clonar o repositório
git clone https://github.com/seu_usuario/icoer-auditoria-mvp.git
cd icoer-auditoria-mvp

# Instalar dependências
pip install -r requirements.txt
python -m spacy download pt_core_news_sm

# Executar notebook de auditoria
jupyter notebook notebooks/notebook_icoer_mvp.ipynb
```

---

## 📄 Licença

MIT License

---

## 🔗 Artigos Relacionados

- [The Informational Coherence Index v7: Real-Time Integration of Bioinformational Signals and Adaptive AI in Distributed Networks](https://doi.org/10.5281/zenodo.15848219)
- [Narratons: Fundamental Units of Coherent Narrative in the Unified Theory of Informational Spin (TGU)](https://doi.org/10.5281/zenodo.15832649)
