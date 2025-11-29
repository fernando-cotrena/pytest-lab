# api_clients/env.py

import os
from dotenv import load_dotenv

# Cargar variables desde .env (y también usar las del sistema)
load_dotenv()

def get_base_url() -> str:
    """
    Devuelve la base URL usada para las peticiones a la API.
    Si no está definida, lanza un error.
    """
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("La variable de entorno BASE_URL no está definida.")
    return base_url.rstrip("/")
