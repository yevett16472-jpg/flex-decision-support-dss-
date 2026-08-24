import os
import sqlite3

def run_diagnostic():
    print("--- STARTING SYSTEM DIAGNOSTIC ---")
   
    # 1. Check for database existence
    db_name = "flex_system.db"
    if not os.path.exists(db_name):
        print(f"[CRITICAL] Database file '{db_name}' not found in current directory.")
        return

    # 2. Check table structure
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [t[0] for t in cursor.fetchall()]
        print(f"[INFO] Tables found: {tables}")
       
        if "Pasadena_Surges" not in tables:
            print("[CRITICAL] Table 'Pasadena_Surges' is missing or corrupted.")
        else:
            print("[SUCCESS] Database schema validated.")
        conn.close()
    except Exception as e:
        print(f"[CRITICAL] Database connection error: {e}")

    # 3. Check for file path inconsistencies (scripts vs DB)
    scripts_to_check = ['surge_ingestion.py', 'surge_visualizer.py', 'flex_db_manager.py']
    for script in scripts_to_check:
        if os.path.exists(script):
            with open(script, 'r') as f:
                content = f.read()
                if "flex_system.db" not in content:
                    print(f"[WARNING] '{script}' may be pointing to the wrong database name.")
                else:
                    print(f"[SUCCESS] '{script}' references correct database.")
        else:
            print(f"[ERROR] Script '{script}' not found.")

    print("--- DIAGNOSTIC COMPLETE ---")

if __name__ == "__main__":
    run_diagnostic()