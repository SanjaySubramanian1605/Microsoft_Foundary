from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["API_KEY"]


llm = init_chat_model(
    model="azure_ai:gpt-4.1-mini",
    base_url = os.environ["llm_endpoint"],
    api_key=api_key
)

print(llm.invoke("What is the capital of France?"))