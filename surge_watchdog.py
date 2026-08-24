import sqlite3
import time
from plyer import notification # Ensure you have this installed via: pip install plyer

DB_NAME = "flex_system.db"
THRESHOLD = 100.0  # Set your surge target here

def check_for_surges():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Look for new entries marked PENDING
        cursor.execute("SELECT id, offer_amount FROM Pasadena_Surges WHERE status = 'PENDING'")
        rows = cursor.fetchall()
       
        for row in rows:
            surge_id, amount = row
            if amount >= THRESHOLD:
                trigger_alert(amount)
                # Mark as notified so we don't spam you
                cursor.execute("UPDATE Pasadena_Surges SET status = 'NOTIFIED' WHERE id = ?", (surge_id,))
                conn.commit()
        conn.close()
    except Exception as e:
        print(f"[ERROR] Watchdog loop failed: {e}")

def trigger_alert(amount):
    notification.notify(
        title="FLEX SURGE DETECTED",
        message=f"New surge of ${amount} is ready for manual review.",
        app_name="MindBodyShop_DSS",
        timeout=10
    )
    print(f"[ALERT] Surge of ${amount} pushed to system.")

if __name__ == "__main__":
    print("--- WATCHDOG ACTIVE: Monitoring flex_system.db ---")
    while True:
        check_for_surges()
        time.sleep(10) # Checks every 10 seconds
        