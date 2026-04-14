import os
import socket
from dotenv import load_dotenv
load_dotenv()

# Extract the host from the URL
url = os.getenv("SUPABASE_DB_URL")
# This is a bit of a hack to get the host out of the string
host = url.split('@')[1].split(':')[0] 

print(f"Testing connection to host: {host}")

try:
    socket.gethostbyname(host)
    print("✅ DNS Resolution successful! Your network can find the database.")
except Exception as e:
    print(f"❌ DNS Resolution failed: {e}")