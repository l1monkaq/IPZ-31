import os
from dotenv import load_dotenv

load_dotenv()

def run_task():
    db = os.getenv("DB_URL")
    key = os.getenv("API_KEY")
    
    if not db or not key:
        print("Error: Config missing!")
        return

    print(f"Connecting to: {db}")
    print(f"API Access: {key[:3]}***")

if __name__ == "__main__":
    run_task()