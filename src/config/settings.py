from dotenv import load_dotenv
import os

load_dotenv()

def get_base_url():
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("BASE_URL no está definido en las variables de entorno.")
    return base_url

def get_token():
    token = os.getenv("AUTH_TOKEN")
    if not token:
        raise ValueError("AUTH_TOKEN no está definido en las variables de entorno.")
    return token