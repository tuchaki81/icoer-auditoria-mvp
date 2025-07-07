import streamlit as st
import pandas as pd
from app.ingestion import load_csv
from app.preprocessing import preprocess_texts
from app.compute_icoer import compute_icoer
from app.reporting import save_report

st.set_page_config(page_title="ICOER Auditoria Ética de IA", layout="wide")

st.title("🧠 ICOER v7 - Auditoria Ética de Modelos de Linguagem")

uploaded_file = st.file_uploader("Faça upload de um arquivo .csv com uma coluna chamada 'text'", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "text" not in df.columns:
        st.error("❌ O arquivo precisa ter uma coluna chamada 'text'")
    else:
        st.success("✅ Arquivo carregado com sucesso!")

        texts = df["text"].dropna().tolist()
        with st.spinner("Pré-processando os textos..."):
            cleaned_texts = preprocess_texts(texts)

        with st.spinner("Calculando o índice ICOER..."):
            result = compute_icoer(cleaned_texts)

        st.subheader("📊 Resultados:")
        st.metric("Coerência Léxico-Semântica", f"{result['coerencia_lexico_semantica']:.4f}")
        st.metric("Entropia Textual Média", f"{result['entropia_textual_media']:.4f}")
        st.metric("ICOER v7 (Simplificado)", f"{result['icoer_v7_simplificado']:.4f}")

        if st.button("💾 Salvar relatório"):
            save_report(result)
            st.success("Relatório salvo como 'icoer_report.txt'")
