import sqlite3
import time
from playwright.sync_api import sync_playwright

# Configuration: Must match your existing system
DB_NAME = "flex_system.db"
TABLE_NAME = "Pasadena_Surges"
TARGET_URL = "https://flex.amazon.com/offers"

def log_to_db(offer_amount, multiplier):
    """Logs data to the central database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f'''
            INSERT INTO {TABLE_NAME} (offer_amount, surge_multiplier, status)
            VALUES (?, ?, 'PENDING')
        ''', (offer_amount, multiplier))
        conn.commit()
        conn.close()
        print(f"[DB] Logged: ${offer_amount} | Multiplier: {multiplier}")
    except Exception as e:
        print(f"[ERROR] Database write failed: {e}")

def run_listener():
    """Launches the automated browser to monitor the offer feed."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
       
        print("[LISTENER] Navigating to Amazon Flex...")
        page.goto(TARGET_URL)
       
        # This keeps the browser open for you to log in
        print("[ACTION] Please log in to your Flex account in the browser.")
        page.wait_for_url("**/offers", timeout=60000)
        print("[SUCCESS] Logged in. Monitoring for surges...")
       
        # Infinite loop to keep the listener active
        while True:
            # Here, the script will eventually scan the offer table
            # For now, it stays alive to maintain your session
            page.wait_for_timeout(5000) # Check every 5 seconds
           
        browser.close()

if __name__ == "__main__":
    run_listener()