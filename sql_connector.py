import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv("DB_User"),
    password=os.getenv("Password"),
    database="FASTAPITOT"
)

def make_connection():
    return conn