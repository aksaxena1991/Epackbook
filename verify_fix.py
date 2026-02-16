import sys
import os
from sqlalchemy import create_engine, text, inspect

# Add project root to sys.path
sys.path.append(os.getcwd())

from main import create_tables
from session import engine

def verify_tables():
    print("Attempting to create tables...")
    try:
        create_tables()
        print("create_tables() executed successfully.")
    except Exception as e:
        print(f"FAILED to create tables: {e}")
        return

    print("Verifying tables in database...")
    inspector = inspect(engine)
    tables = inspector.get_table_names(schema="public")
    print(f"Tables in 'public' schema: {tables}")
    
    if "auth" in tables and "auth_sessions" in tables:
        print("SUCCESS: All expected tables found in 'public' schema.")
    else:
        print("FAILURE: Expected tables missing.")

if __name__ == "__main__":
    verify_tables()
