import sqlite3
import os

def initialize_database(db_name="flex_system.db"):
    # Remove the existing file to clear any corruption
    if os.path.exists(db_name):
        os.remove(db_name)
        print(f"Existing file {db_name} removed.")

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the Pasadena_Surges table
    cursor.execute('''
        CREATE TABLE Pasadena_Surges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            offer_amount REAL,
            surge_multiplier REAL,
            status TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database '{db_name}' initialized successfully with 'Pasadena_Surges' table.")

if __name__ == "__main__":
    initialize_database()