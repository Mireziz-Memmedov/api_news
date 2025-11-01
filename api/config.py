from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")

if not API_KEY:
    raise ValueError("GNEWS_API_KEY not found in env file.")

