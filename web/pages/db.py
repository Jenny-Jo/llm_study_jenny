import streamlit as st
from dotenv import load_dotenv
from common.service.film_service import get_film_list
load_dotenv()

#########################
# 화면 영역
#########################
df, title = get_film_list()

st.title(title)
st.dataframe(df)
