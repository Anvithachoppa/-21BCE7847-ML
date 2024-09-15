from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_project = os.getenv("LANGCHAIN_PROJECT")
langchain_tracking_v2 = os.getenv("LANGCHAIN_TRACKING_V2")

# Print values to verify they are loaded
print(f"LANGCHAIN_API_KEY: {langchain_api_key}")
print(f"OPENAI_API_KEY: {openai_api_key}")
print(f"LANGCHAIN_PROJECT: {langchain_project}")
print(f"LANGCHAIN_TRACKING_V2: {langchain_tracking_v2}")
