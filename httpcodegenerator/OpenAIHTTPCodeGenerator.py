from .HTTPCodeGenerator import HTTPCodeGenerator, HTTPCodeCandidate
from pydantic import BaseModel
import marvin

class OpenAIHTTPCodeGenerator(HTTPCodeGenerator):
    def __init__(self, api_key: str):
        marvin.settings.openai.api_key = api_key
    def generate_codes(self, action: str) -> list[HTTPCodeCandidate]:
        candidates_res = generate_codes(action)
        if candidates_res.error:
            raise Exception(candidates_res.error)
        return candidates_res.candidates

class HTTPCodeCandidateResponse(BaseModel):
    candidates: list[HTTPCodeCandidate]
    error: str | None

@marvin.fn
def generate_codes(action: str) -> HTTPCodeCandidateResponse:
    """
    Generate a list of suitable HTTP status codes for the `action` provided by the user. 
    Else return an error message if an http code is not applicable.
    """      