import sqlite3
import pandas as pd

# Central Configuration
DB_NAME = "flex_system.db"

def display_surges():
    """Visualizes current pending surges from the system."""
    try:
        conn = sqlite3.connect(DB_NAME)
        query = "SELECT * FROM Pasadena_Surges ORDER BY timestamp DESC LIMIT 10"
        df = pd.read_sql_query(query, conn)
        conn.close()
       
        if df.empty:
            print("[INFO] No surge data currently in system.")
        else:
            print("--- CURRENT SURGE DATA ---")
            print(df)
    except Exception as e:
        print(f"[ERROR] Visualization failure: {e}")

if __name__ == "__main__":
    display_surges()