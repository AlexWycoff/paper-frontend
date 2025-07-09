import streamlit as st
import sys
sys.path.insert(1, "paper-frontend/functions.py")
from functions import *

st.set_page_config(page_title="Search")

if 'search' not in st.session_state.keys():
    st.session_state['search'] = ""
st.text_input("Find gaps in research on any topic", key="search", value=st.session_state['search'])
search_input = st.session_state['search']

with st.sidebar:
    st.logo("logo.png")

if search_input != "":
    with st.spinner("Generating Query...", show_time=True):
        query = prompt_query(search_input)
        st.write("**Boolean Search Query:**")
        st.write(query)
    with st.spinner("Searching for articles...", show_time=True):
        paper_df = core_query(query.replace("|", "OR"), limit=10)
        st.dataframe(paper_df.iloc[:, [0, 4]])
    with st.spinner("Analyzing articles...", show_time=True):
        st.write_stream(research_query(search_input, paper_df))
        for i in range(len(paper_df)):
            st.write(f"    {paper_df.loc[i, 'citation']} \n\n")