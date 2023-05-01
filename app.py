import streamlit as st
import pandas as pd
from Utils import *


st.set_page_config(page_title="Topic List", layout="centered")
st.title("Create List")
st.session_state['input_topic'] = ''

input_topic = st.text_input("Enter a topic:", key= "text", value="")

st.header("Topics and Counts")
count_placeholder = st.empty()
sort_state = st.session_state.get('sort_state', False)


# table_placeholder = st.empty()
col1, colX,col2 = st.columns((1, 3, 1))

if col1.button("Remove Topic"):
    st.session_state['data'] = remove_topic(input_topic)
else:
    st.session_state['data'] = update_topic_counts(input_topic)
    st.session_state['sort_state'] = False


if col2.button("Sort by Count", on_click=clear_text):

    sort_state = not sort_state
    st.session_state['data'] = sort_by_count(st.session_state['data'], sort_state)
    st.session_state['sort_state'] = sort_state

count_placeholder.write(f"Total Topics: {len(st.session_state['data'].index)-1}")
st.table(st.session_state['data'])