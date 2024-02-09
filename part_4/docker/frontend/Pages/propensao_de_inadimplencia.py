from urllib import response
import requests
import streamlit as st
import json

def dados_inadimplencia(body):
    with open('/myServer/config/microservices.json') as json_file:
        microservices_config = json.load(json_file)

    url = f'{microservices_config["model_manager"]["endpoint"]}/predict?model=default_propensity'
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
    with st.form("loan_application_form"):
        occupancy_type = st.selectbox('Occupancy Type', options=['pr', 'ir', 'sr'])
        co_applicant_credit_type = st.selectbox('Co-Applicant Credit Type', options=['EXP', 'CIB'])
        credit_score = st.number_input('Credit Score', min_value=0.0, max_value=1000.0)
        ltv = st.number_input('LTV', min_value=0, max_value=10000)
        loan_purpose = st.selectbox('Loan Purpose', options=['p1', 'p4', 'p3', 'p2'])
        dtir1 = st.number_input('DTIR1', min_value=0.0, max_value=100.0)
        property_value = st.number_input('Property Value', min_value=8000.0, max_value=16508000.0)
        submission_of_application = st.selectbox('Submission of Application', options=['to_inst', 'not_inst'])
        approv_in_adv = st.selectbox('Approval in Advance', options=['nopre', 'pre'])
        income = st.number_input('Income', min_value=0.0, max_value=578580.0)
        
        submitted = st.form_submit_button("Executar")
        if submitted:
            body = {
            'occupancy_type': f"{occupancy_type}",
            'co_applicant_credit_type': f"{co_applicant_credit_type}",
            'Credit_Score': float(credit_score),
            'LTV': float(ltv),
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
                
