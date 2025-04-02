import enum
from typing import Iterator, List, Dict, Any
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from common.screen.constant import ROLE_TYPE, HISTORY_INFO
from common.llm.provider import BaseProvider

class OLLAMA_LLMs(enum.Enum):
    gemma3_1b = (enum.auto(), "gemma3:1b")
    gemma3_q8 = (enum.auto(), "gemma3-q8")
    gemma3_1b2 = (enum.auto(), "gemma3:1b2")
    gemma3_1b3 = (enum.auto(), "gemma3:1b3")

class OllamaProvider(BaseProvider):
    def _create_client(self):
        return None  # Ollama는 로컬에서 실행되므로 별도의 클라이언트 생성 불필요

    def _get_model_name(self, model_id: str) -> str:
        return getattr(OLLAMA_LLMs, model_id).value[1]

    def stream_response(self, model_id: str, messages: List[Dict[str, Any]]) -> Iterator[str]:
        llm = ChatOllama(model=self._get_model_name(model_id))
        prompts = []

        for message in messages[:-1]:  # user message 제외
            prompts.append(tuple(message.values()))
        prompts += [(ROLE_TYPE.user.name, "{user_input}")]
        
        chat_prompt = ChatPromptTemplate.from_messages(prompts)
        chain = chat_prompt | llm | StrOutputParser()
        
        for token in chain.stream({"user_input": messages[-1][HISTORY_INFO.content.name]}):
            yield token
            self._sleep() 
