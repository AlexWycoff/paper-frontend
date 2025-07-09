import pandas as pd
import numpy as np
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="Main")

with st.sidebar:
    st.logo("logo.png")
    
st.markdown("<h1 style='text-align: center;'>Paper AI</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Explore gaps in literature with just a few clicks</h6>", unsafe_allow_html=True)

# Selectboxes for choosing a research topic

research_categories = pd.read_csv("ResearchCategories.csv", index_col=0)

st.selectbox("Start by choosing your research discipline", 
             np.unique(research_categories['Discipline']), 
             index=None, 
             key="Discipline")

discipline = st.session_state['Discipline']

if discipline != None:
    st.selectbox("Now select a field within your discipline", 
                 np.unique(research_categories[research_categories['Discipline'] == discipline]['Field']), 
                 index=None, 
                 key="Field")
    field = st.session_state['Field']
    
    if field != None:
        st.selectbox("Then choose your topic", 
                     np.unique(research_categories[research_categories['Field'] == field]['Topic']), 
                     index=None, 
                     key="Topic")
        topic = st.session_state['Topic']
        
        if topic != None:
            with stylable_container(
                key="Search_button",
                css_styles="""
                button{
                    margin: 0 auto;
                    display: block;
                }
                """
            ):
                submit = st.button("Search for Gaps in Research")
            
            if submit:
                st.session_state['search'] = topic
                st.switch_page("pages/Search.py")