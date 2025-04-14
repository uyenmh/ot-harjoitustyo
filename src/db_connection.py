import sqlite3
from config import DB_FILE_PATH


db_connection = sqlite3.connect(DB_FILE_PATH)
db_connection.row_factory = sqlite3.Row

def get_db_connection():
    return db_connection
