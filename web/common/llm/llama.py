import enum
from groq import Groq
from typing import Iterator, List, Dict, Any
from common.llm.provider import BaseProvider

class GROQ_LLMs(enum.Enum):
    llama3 = (enum.auto(), "llama-3.3-70b-versatile") 
    qwen = (enum.auto(), "qwen-qwq-32b")

class GroqProvider(BaseProvider):
    def _create_client(self):
        return Groq(api_key=self.api_key)

    def _get_model_name(self, model_id: str) -> str:
        return getattr(GROQ_LLMs, model_id).value[1]

    def stream_response(self, model_id: str, messages: List[Dict[str, Any]]) -> Iterator[str]:
        response = self.client.chat.completions.create(
            model=self._get_model_name(model_id),
            messages=messages,
            stream=True
        )
        for token in response:
            if token.choices[0].delta.content is not None:
                yield token.choices[0].delta.content
                self._sleep()
