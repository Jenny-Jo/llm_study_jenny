import streamlit as st
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

st.title("DB 연동 테스트")

conn = st.connection(
    type="sql",
    name="mydb",
    dialect="postgresql",
    host=os.getenv("host"),
    port=os.getenv("port"),
    database=os.getenv("database"),
    username=os.getenv("uname"),
    password=os.getenv("password")
)

sql = """
select f1.film_id,
	   f1.title,
	   count(f2.actor_id) as actor_cnt
from film f1
left join film_actor f2
on f1.film_id = f2.film_id
group by f1.film_id"""

df = conn.query(sql, ttl=10)

st.dataframe(df)
