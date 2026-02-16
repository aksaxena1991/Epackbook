import sys
import os
from sqlalchemy import create_engine, text

# Add project root to sys.path
sys.path.append(os.getcwd())

from settings import settings

def debug_database():
    print(f"Connecting to: {settings.DATABASE_URL}")
    engine = create_engine(settings.DATABASE_URL)
    
    try:
        with engine.connect() as connection:
            print("Successfully connected!")
            
            # Check current user and database
            user = connection.execute(text("SELECT current_user")).scalar()
            db = connection.execute(text("SELECT current_database()")).scalar()
            print(f"User: {user}")
            print(f"Database: {db}")
            
            # Check search_path
            search_path = connection.execute(text("SHOW search_path")).scalar()
            print(f"Search Path: {search_path}")
            
            # Check current schema
            current_schema = connection.execute(text("SELECT current_schema()")).scalar()
            print(f"Current Schema: {current_schema}")
            
            # List all schemas
            print("\nAvailable Schemas:")
            schemas = connection.execute(text("SELECT schema_name FROM information_schema.schemata")).fetchall()
            for schema in schemas:
                print(f" - {schema[0]}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_database()
