import sqlite3
from datetime import datetime

# Central Configuration
DB_NAME = "flex_system.db"
TABLE_NAME = "Pasadena_Surges"

def log_surge_data(offer_amount, surge_multiplier):
    """Logs incoming surge data into the unified system."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(f'''
            INSERT INTO {TABLE_NAME} (offer_amount, surge_multiplier, status)
            VALUES (?, ?, ?)
        ''', (offer_amount, surge_multiplier, 'PENDING'))
        conn.commit()
        conn.close()
        print(f"[SUCCESS] Logged surge: ${offer_amount} at {datetime.now()}")
    except Exception as e:
        print(f"[ERROR] Ingestion failure: {e}")

if __name__ == "__main__":
    # Test Ingestion
    log_surge_data(120.50, 1.5)