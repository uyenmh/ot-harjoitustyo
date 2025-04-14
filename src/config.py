import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

dotenv_path = os.path.join(dirname, "..", ".env")
load_dotenv(dotenv_path)

DB_FILENAME = os.getenv("DB_FILENAME") or "sudoku_db.sqlite"

DB_FILE_PATH = os.path.join(dirname, "..", "data", DB_FILENAME)
