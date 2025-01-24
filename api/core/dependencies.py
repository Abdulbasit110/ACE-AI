from langchain.llms import OpenAI
from api.core.config import settings

def get_openai_client():
    return OpenAI(api_key=settings.OPENAI_API_KEY)
