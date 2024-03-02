import streamlit as st
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

st.form:
    st.number_input("Health", 0, 50, 50)
    st.number_input("Focus", 0, 30, 30)
