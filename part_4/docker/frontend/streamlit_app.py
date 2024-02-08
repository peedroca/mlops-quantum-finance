from urllib import response
import requests
import streamlit as st
import json
import Pages.propensao_de_inadimplencia as page_ina
import Pages.clusterizacao_e_classificacao as page_clust
import Pages.Inicio as page_inicio

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def ui():
    Page_cliente = st.sidebar.selectbox(
    'Menu', ['Inicio','Avaliação de Crédito', 'Propensão de Inadimplência'], 0)

    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    if Page_cliente == 'Avaliação de Crédito':
        page_clust.customer_clustering()

    if Page_cliente == 'Propensão de Inadimplência':
        page_ina.propensao_de_inadimplencia()

    if Page_cliente == 'Inicio':
        page_inicio.inicio()
    

ui()
