from .HTTPCodeGenerator import HTTPCodeGenerator
from .OpenAIHTTPCodeGenerator import OpenAIHTTPCodeGenerator
import os

class HTTPCodeGeneratorFactory:
    @staticmethod
    def create_generator() -> HTTPCodeGenerator:
        api_key = os.getenv("OPENAI_API_KEY")
        return OpenAIHTTPCodeGenerator(api_key)