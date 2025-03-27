import streamlit as st 

from common.screen.history import init_history, add_history
from common.screen.display import print_history_message, print_message
from common.screen.input import get_prompt, chosen_llms, chosen_provider
from common.llm.call_provider import get_response_from_llm, PROVIDER_TYPE
from common.screen.constant import ROLE_TYPE
from common.screen.utils import init_display,init_page

def app():
  st.title("Chatbot")

  # 세션 상태 초기화
  init_page()
  chosen_provider, chosen_llm = init_display()

# 사용자의 메세지 
  prompt = get_prompt()

  if prompt is not None:
    # 사용자 메시지를 세션 상태에 추가
    add_history(ROLE_TYPE.user, prompt)
    
    # 사용자 메시지 표시
    print_message(ROLE_TYPE.user.name, prompt)
    
    # AI 응답을 세션 상태에 추가
    generator = get_response_from_llm(
      chosen_provider=PROVIDER_TYPE[chosen_provider]
      , messages=st.session_state.messages, 
      llm_name=chosen_llm)
    # AI 응답 표시
    assistant_message = print_message(
      ROLE_TYPE.assistant.name
      , generator
    )
    
    add_history(ROLE_TYPE.assistant, assistant_message)

if __name__ == "__main__":
  app()
