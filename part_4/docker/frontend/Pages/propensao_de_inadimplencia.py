from urllib import response
import requests
import streamlit as st
import json

BASE_URL = "http://172.214.88.215"

def dados_inadimplencia(body):
    url = f'{BASE_URL}/predict?model=default_propensity'
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

def propensao_de_inadimplencia():
    icon("🏦")
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Propensão de Inadimplência')
    occupancy_type = st.text_input('Insira o occupancy_type:')
    co_applicant_credit_type = st.text_input('Insira o co_applicant_credit_type:')
    credit_Score = st.text_input('Insira o Credit_Score:')
    lvt = st.text_input('Insira o LVT:')
    loan_purpose = st.text_input('Insira o loan_purpose:')
    dtir1 = st.text_input('Insira o dtir1:')
    property_value = st.text_input('Insira o property_value:')
    submission_of_application = st.text_input('Insira o submission_of_application:')
    approv_in_adv = st.text_input('Insira o approv_in_adv:')
    income = st.text_input('Insira o income:')

    
    if st.button('Executar'):
        body = {
        'occupancy_type': f"{occupancy_type}",
        'co_applicant_credit_type': f"{co_applicant_credit_type}",
        'Credit_Score': float(credit_Score),
        'LTV': float(lvt),
        'loan_purpose': f"{loan_purpose}",
        'dtir1': float(dtir1),
        'property_value': float(property_value),
        'submission_of_application': f"{submission_of_application}",
        'approv_in_adv': f"{approv_in_adv}",
        'income': float(income)
        }

        retorno = dados_inadimplencia(body)
        if retorno is not None:
            if retorno['prediction'] == 0:
                st.write('Sem propensão a inadimplência')
            else:
                st.write('Com propensão a inadimplência')
                
