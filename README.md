# 🤖 Agente de IA - Vendas

Projeto desenvolvido em Python para análise de planilhas de vendas utilizando **Pandas, Streamlit e Google Gemini**.

A aplicação permite que o usuário envie uma planilha Excel (`.xlsx`), visualize seus dados e faça perguntas em linguagem natural. A IA analisa os dados da planilha e retorna uma resposta de forma simples e direta.

## 🚀 Funcionalidades

* 📂 Upload de planilhas Excel (`.xlsx`)
* 📊 Visualização dos dados utilizando Pandas e Streamlit
* 🔎 Consulta dos dados através de perguntas em linguagem natural
* 🤖 Integração com a API do Google Gemini
* 💬 Respostas baseadas nos dados da planilha

## 🛠️ Tecnologias utilizadas

* **Python**
* **Streamlit** — criação da interface web
* **Pandas** — leitura e manipulação dos dados
* **OpenPyXL** — leitura de arquivos Excel
* **Google Gemini API** — análise dos dados utilizando Inteligência Artificial
* **JSON** — armazenamento da chave da API

## 📋 Como funciona

O funcionamento do projeto segue este fluxo:

```text
Planilha Excel
      ↓
   Streamlit
      ↓
     Pandas
      ↓
  Dados da planilha
      ↓
 Pergunta do usuário
      ↓
   Google Gemini
      ↓
     Resposta
```

## 💻 Instalação

Clone o repositório:

```bash
git clone https://github.com/jaktmo-star
```

Entre na pasta do projeto:

```bash
cd vendas
```

Instale as bibliotecas necessárias:

```bash
pip install streamlit pandas openpyxl google-genai
```

## 🔑 Configuração da API

Crie um arquivo chamado:

```text
token.json
```

Dentro dele, coloque sua chave da API:

```json
{
    "api_key": "SUA_CHAVE_AQUI"
}
```

**Importante:** nunca publique sua chave da API no GitHub.

Adicione o arquivo `token.json` ao `.gitignore`:

```text
token.json
```

## ▶️ Executando o projeto

No terminal, execute:

```bash
streamlit run vendas.py
```

Depois, abra o endereço apresentado pelo Streamlit no navegador.

## 📊 Exemplo de utilização

Após enviar uma planilha de vendas, o usuário pode fazer perguntas como:

```text
Qual produto vendeu mais?
```

```text
Qual foi o total de vendas?
```

```text
Qual vendedor realizou mais vendas?
```

A aplicação envia os dados e a pergunta para o modelo de IA e apresenta a resposta na interface.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como parte do meu aprendizado em **Python, análise de dados, APIs e Inteligência Artificial**, buscando aplicar esses conhecimentos em uma situação prática de análi
