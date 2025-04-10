import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Obtener valores del entorno
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database_name = os.getenv("DB_NAME")

# Conexión
database = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database_name
)
