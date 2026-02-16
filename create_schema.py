import sys
import os
from sqlalchemy import create_engine, text

# Add project root to sys.path
sys.path.append(os.getcwd())

from settings import settings

def create_schema():
    print(f"Connecting to: {settings.DATABASE_URL}")
    engine = create_engine(settings.DATABASE_URL)
    
    try:
        with engine.connect() as connection:
            print("Creating 'public' schema...")
            connection.execute(text("CREATE SCHEMA IF NOT EXISTS public"))
            connection.commit()
            print("Successfully created 'public' schema!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_schema()
