import enum
import time
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from common.screen.constant import ROLE_TYPE, HISTORY_INFO

class OLLAMA_LLMs(enum.Enum):

  gemma3_1b = (enum.auto(), "gemma3:1b")

def ClientOllama(
    model_name,
    messages,
    stream=True
):
    llm = ChatOllama(model=OLLAMA_LLMs[model_name].value[1])
    prompts = []

    for message in messages[:-1]: # user message 제외
        prompts.append(tuple(message.values()))
    prompts += [(ROLE_TYPE.user.name, "{user_input}")]
    
    chat_prompt = ChatPromptTemplate.from_messages(prompts)

    chain = chat_prompt | llm | StrOutputParser()
    for token in chain.stream({"user_input": messages[-1][HISTORY_INFO.content.name]}):
        yield token
        time.sleep(0.05) 
