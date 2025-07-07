# ICOER MVP — Auditoria Ética de LLMs

Este projeto implementa um MVP para calcular o Índice de Coerência Informacional (ICOER v7) em saídas de modelos de linguagem natural (LLMs), com foco em auditoria ética automatizada.

## Estrutura

- `app/`: Módulos principais de processamento e cálculo
- `data/raw/`: Dados de entrada para auditoria
- `notebooks/`: Execução interativa via Jupyter
- `tests/`: Testes unitários com pytest

## Requisitos

Instale com:

```bash
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
```

## Execução

1. Prepare um arquivo `.csv` com uma coluna chamada `text`
2. Execute o notebook `notebooks/notebook_icoer_mvp.ipynb` para análise completa
3. Gere um relatório com as métricas de coerência
4. Execute `pytest` para validar o funcionamento

## Licença

MIT License
