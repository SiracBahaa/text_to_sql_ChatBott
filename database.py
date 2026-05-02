import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
db_path = os.getenv('DB_PATH')

# Connect to the SQLite database and create a cursor
con = sqlite3.connect(db_path, check_same_thread=False)
cur = con.cursor()

def execute_query(query):
    """Executes a query and returns the results."""
    cur.execute(query)
    # Commit the transaction if the query is not a SELECT query
    if query.strip().upper().startswith("INSERT") or \
       query.strip().upper().startswith("UPDATE") or \
       query.strip().upper().startswith("DELETE") or \
       query.strip().upper().startswith("CREATE") or \
       query.strip().upper().startswith("DROP") or \
       query.strip().upper().startswith("ALTER") or \
       query.strip().upper().startswith("TRUNCATE") or \
       query.strip().upper().startswith("RENAME") : 
       con.commit()
    return cur.fetchall()