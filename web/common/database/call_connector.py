import streamlit as st
import os

#########################
# DB 영역
#########################
@st.cache_resource 
# 캐시에 저장된 리소스를 사용하여 성능 향상/ connection 객체는 메모리에 저장되어 있음
# 여러번 호출해도 한번만 실행됨
def get_connector():
    return st.connection(
    type="sql",
    name="mydb",
    dialect="postgresql",
    host=os.getenv("host"),
    port=os.getenv("port"),
    database=os.getenv("database"),
    username=os.getenv("uname"),
    password=os.getenv("password")
    )
