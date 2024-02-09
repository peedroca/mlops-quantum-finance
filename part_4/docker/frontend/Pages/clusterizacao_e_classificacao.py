from urllib import response
import requests
import streamlit as st
import json
import sys, os, io, uuid, datetime, json, zipfile

def dados_clusteringa(body):
    with open('/myServer/config/microservices.json') as json_file:
        microservices_config = json.load(json_file)

    url = f'{microservices_config["model_manager"]["endpoint"]}/predict?model=customer_clustering'
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
    with st.form("loan_details_form"):
        loan_purpose = st.selectbox('Loan Purpose', options=['p1', 'p4', 'p3', 'p2'])
        security_type = st.selectbox('Security Type', options=['direct', 'Indriect'])
        age = st.selectbox('Applicant Age Group', options=['55-64', '45-54', '35-44', '>74', '25-34', '65-74', '<25'])
        region = st.selectbox('Region', options=['North', 'central', 'south', 'North-East'])

        year = st.number_input('Year', min_value=2010, max_value=2030, value=2024)  # Assuming fixed year
        loan_amount = st.number_input('Loan Amount', min_value=0.0, max_value=3576500.0)
        term = st.number_input('Term (in months)', min_value=1, max_value=360)
        property_value = st.number_input('Property Value', min_value=8000.0, max_value=16508000.0)
        income = st.number_input('Applicant Income', min_value=0.0, max_value=578580.0)
        credit_score = st.number_input('Credit Score', min_value=0.0, max_value=1000.0)
        ltv = st.number_input('LTV (Loan to Value ratio)', min_value=0, max_value=10000)
        dtir1 = st.number_input('DTIR1 (Debt-to-Income Ratio)', min_value=0.0, max_value=100.0)

        submitted = st.form_submit_button("Submit")
        if submitted:
            body = {
            'loan_purpose': f"{loan_purpose}",
            'Security_Type': f"{security_type}",
            'age': f"{age}",
            'Region': f"{region}",
            'year': int(year),
            'loan_amount': int(loan_amount),
            'term': float(term),
            'property_value': float(property_value),
            'income': float(income),
            'Credit_Score': int(credit_score),
            'LTV': float(ltv),
            'dtir1': float(dtir1)
        }

            retorno = dados_clusteringa(body)
            if retorno is not None:
                st.write(retorno)

