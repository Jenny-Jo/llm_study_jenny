import enum
import time


from common.llm.openai import OPENAI_LLMs, ClientOpenAI
from common.llm.llama import GROQ_LLMs, ClientGroq
from common.llm.ollama import OLLAMA_LLMs, ClientOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class PROVIDER_TYPE(enum.Enum):
  # 제공자명 = (인덱스, 호출함수, 사용가능한 모델 리스트)
  groq = (enum.auto(), ClientGroq, GROQ_LLMs)
  openai = (enum.auto(), ClientOpenAI, OPENAI_LLMs)
  ollama = (enum.auto(), ClientOllama, OLLAMA_LLMs)


def get_response_from_llm(chosen_provider:PROVIDER_TYPE, messages, llm_name:str):
  if not isinstance(chosen_provider, PROVIDER_TYPE):
    raise Exception("허락한 제공자가 아닙니다.") 
  elif llm_name not in chosen_provider.value[2].__members__:
    raise Exception("허락한 모델명이 아닙니다.") 

  for token in chosen_provider.value[1](llm_name, messages):
    yield token
    time.sleep(0.05)





