
📝 README.md

# 🔍 API Test Automation with Pytest

Este proyecto contiene pruebas automatizadas para validar el endpoint de importación de personas usando `pytest`, `requests` y buenas prácticas de configuración.

---

## 🚀 Requisitos

- Python 3.8 o superior
- `pip` o `pipenv` para manejar dependencias
- Acceso a un endpoint API válido
- Token de autenticación para el entorno

---

## 📦 Instalación

Cloná el repo y luego instalá las dependencias:

```bash
pip install -r requirements.txt

    Asegurate de tener activado tu entorno virtual (recomendado con venv, virtualenv, pipenv o poetry).

⚙️ Configuración del entorno

    Copiá el archivo de plantilla .env_template y renombralo a .env:

cp .env_template .env

    Completá las variables en .env con tus datos reales:

# .env
BASE_URL=https://api.qa.worldsts.ar

🧪 Correr los tests
✔️ Todos los tests

pytest -v

📝 Generar un reporte HTML

pytest --html=report.html --self-contained-html

El archivo report.html contendrá el resumen de ejecución, errores y resultados.
🛠 Estructura del proyecto (resumen)
