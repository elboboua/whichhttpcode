
from abc import ABC, abstractmethod
from pydantic import BaseModel

class HTTPCodeCandidate(BaseModel):
    code: int
    reason: str
    justification: str


class HTTPCodeGenerator(ABC):
    @abstractmethod
    def generate_codes(self, action: str) -> list[HTTPCodeCandidate]:
        pass

