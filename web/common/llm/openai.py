import enum
from openai import OpenAI
from typing import Iterator, List, Dict, Any
from common.llm.provider import BaseProvider

class OPENAI_LLMs(enum.Enum):
    gpt_4o_mini = (enum.auto(), "gpt-4o-mini") 
    gpt_4o = (enum.auto(), "gpt-4o") 

class OpenAIProvider(BaseProvider):
    def _create_client(self):
        return OpenAI(api_key=self.api_key)

    def _get_model_name(self, model_id: str) -> str:
        return getattr(OPENAI_LLMs, model_id).value[1]

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
