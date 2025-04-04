import streamlit as st
from common.llm.openai import OPENAI_LLMs
from common.llm.llama import GROQ_LLMs
from common.llm.call_provider import PROVIDER_TYPE

def chosen_provider():
  chosen_provider = st.sidebar.selectbox(
    label="LLM 제공자를 선택해주세요.",
    options=list(PROVIDER_TYPE.__members__)
  )

  return chosen_provider

def get_prompt():
  return st.chat_input("무엇이든지 물어봐주세요.")


def chosen_llms(choiced_provider:str):
  chosen_llm = st.sidebar.selectbox(
    label="모델을 선택해주세요.",
    options=list(PROVIDER_TYPE[choiced_provider].value[2].__members__)
  )

  return chosen_llm

