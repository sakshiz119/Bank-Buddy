import streamlit as st
from langchain_helper import db_chain

st.title("Bank Buddy 🏦 \n Ask any query relate to Banking: ")

question = st.text_input("Question: ")

if question:
    chain = db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)