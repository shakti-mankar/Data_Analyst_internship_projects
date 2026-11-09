
import streamlit as st

def load_css():
    with open("assets/style.css", "r") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )

def page_header(title, subtitle):
    st.title(title)
    st.caption(subtitle)
    st.divider()
