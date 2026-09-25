# Autor: Elcio Mello
# Projeto: Automação de Vendas com Excel

# Bibliotecas
import streamlit as st
import pandas as pd
import json 
from google import genai

# Configuração 
with open ("token.json") as arquivo:
    token = json.load(arquivo)

client = genai.Client(api_key=token["api_key"])

# Interface 
st.title(" Agente de IA - Vendas")

# Abrir uma planilha especifica
arquivo = st.file_uploader(
    "Escolha a Planilha",
    type=["xlsx"]
)

# Condicional para ler os dados da planilha
if arquivo:
    dados = pd.read_excel(arquivo)
    st.subheader("Dados da planilha")
    st.dataframe(dados)
    pergunta = st.text_input("O que deseja saber?")

    if st.button("Pergunte!") and pergunta:
        contexto = dados.to_string(index=False)

        prompt = f"""
Você é um agente de análise de vendas.
Responda à pergunta usando SOMENTE os dados da planilha abaixo.
Planilha:{contexto}
Pergunta:{pergunta}
Responda de forma simples e direta.
"""

        resposta = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )
        st.subheader("Respostas")
        st.write(resposta.text)