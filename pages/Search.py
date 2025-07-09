import streamlit as st
from functions import *

st.set_page_config(page_title="Search")

if 'search' in st.session_state.keys():
    st.text_input("Find gaps in research on any topic", key="search", value=st.session_state['search'])
else:
    st.text_input("Find gaps in research on any topic", key="search")
search_input = st.session_state['search']

with st.sidebar:
    st.logo("logo.png")

if search_input != "":
    with st.spinner("Searching for articles...", show_time=True):
        query = prompt_query(search_input)
        paper_df = core_query(query.replace("|", "OR"), limit=10)
        st.dataframe(paper_df.iloc[:, [0, 4]])
    with st.spinner("Analyzing articles...", show_time=True):
        st.write_stream(research_query(search_input, paper_df))
        for i in range(len(paper_df)):
            st.write(f"    {paper_df.loc[i, 'citation']} \n\n")