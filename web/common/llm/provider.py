from abc import ABC, abstractmethod
import enum
from typing import Iterator, List, Dict, Any, Type
import time

class BaseProvider(ABC):
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.client = self._create_client()

    @abstractmethod
    def _create_client(self):
        """API 클라이언트 생성"""
        pass

    @abstractmethod
    def _get_model_name(self, model_id: str) -> str:
        """모델 ID를 실제 API 모델명으로 변환"""
        pass

    def stream_response(self, model_id: str, messages: List[Dict[str, Any]]) -> Iterator[str]:
        """스트리밍 응답 생성"""
        pass

    def _sleep(self, seconds: float = 0.05):
        """응답 간 딜레이"""
        time.sleep(seconds)

class Provider:
    def __init__(self, provider_class: Type[BaseProvider], api_key: str = None):
        self.provider = provider_class(api_key)

    def __call__(self, model_name: str, messages: List[Dict[str, Any]]) -> Iterator[str]:
        return self.provider.stream_response(model_name, messages)
