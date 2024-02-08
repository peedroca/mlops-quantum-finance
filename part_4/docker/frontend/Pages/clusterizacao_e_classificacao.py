from urllib import response
import requests
import streamlit as st
import json

BASE_URL = "http://172.214.88.215"

def dados_clusteringa(body):
    url = f'{BASE_URL}/predict?model=customer_clustering'
    headers = {'Content-Type': 'application/json'}  # Adicione os cabeçalhos JSON
    try:
        resposta = requests.post(url, data=json.dumps(body), headers=headers)
        resposta.raise_for_status()  # Lança uma exceção para erros HTTP
        return resposta.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro na requisição: {e}, {json.dumps(body)}")
        return None

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def customer_clustering():
    icon("🏦")
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Avaliação de Crédito')
    loan_purpose = st.text_input('Insira o loan_purpose:')
    Security_Type = st.text_input('Insira o Security_Type:')
    age = st.text_input('Insira o age:')
    Region = st.text_input('Insira o Region:')
    year = st.text_input('Insira o year:')
    loan_amount = st.text_input('Insira o loan_amount:')
    term = st.text_input('Insira o term:')
    property_value = st.text_input('Insira o property_value:')
    income = st.text_input('Insira o income:')
    Credit_Score = st.text_input('Insira o Credit_Score:')
    LTV = st.text_input('Insira o LTV:')
    dtir1 = st.text_input('Insira o dtir1:')

    
    if st.button('Executar'):
        body = {
        'loan_purpose': f"{loan_purpose}",
        'Security_Type': f"{Security_Type}",
        'age': f"{age}",
        'Region': f"{Region}",
        'year': int(year),
        'loan_amount': int(loan_amount),
        'term': float(term),
        'property_value': float(property_value),
        'income': float(income),
        'Credit_Score': int(Credit_Score),
        'LTV': float(LTV),
        'dtir1': float(dtir1)
    }

        retorno = dados_clusteringa(body)
        if retorno is not None:
            st.write(retorno)

