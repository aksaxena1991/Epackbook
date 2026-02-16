import sys
import os

# Add project root to sys.path
sys.path.append(os.getcwd())

from models.base import Base
# Force registration
from models.auth import Auth
from models.auth_session import Auth_Session

print("Schema:", Base.metadata.schema)
print("Tables:", Base.metadata.tables.keys())

# Check for tables (keys might be 'auth' or 'public.auth' depending on config, 
# but we are moving to no schema, so likely just 'auth')
found_auth = any(t.endswith('auth') for t in Base.metadata.tables.keys())
found_session = any(t.endswith('auth_sessions') for t in Base.metadata.tables.keys())

if found_auth:
    print("SUCCESS: auth table found")
else:
    print("FAILURE: auth table NOT found")

if found_session:
    print("SUCCESS: auth_sessions table found")
else:
    print("FAILURE: auth_sessions table NOT found")
