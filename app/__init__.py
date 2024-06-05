import os
from dotenv import load_dotenv

load_dotenv()


openai_config = {
    "api_key": os.getenv("OPENAI_API_KEY"),
}
