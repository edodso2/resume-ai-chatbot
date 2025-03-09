import os
from dotenv import load_dotenv

def load_env():
  # Load from .env for local development only
  if os.path.exists(".env"):
      load_dotenv()

  # Get API key from environment 
  api_key = os.getenv('OPENAI_API_KEY')
  if not api_key:
      raise ValueError("OPENAI_API_KEY not found in environment variables")