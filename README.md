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
