import sqlite3

def get_db_connection():
    return sqlite3.connect('pasadena_surges.db')

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pasadena_Surges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            offer_amount REAL,
            block_time TEXT,
            location TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Database foundation (upgraded) initialized.")

def log_surge(offer_amount, block_time, location, status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Pasadena_Surges (timestamp, offer_amount, block_time, location, status)
        VALUES (CURRENT_TIMESTAMP, ?, ?, ?, ?)
    """, (offer_amount, block_time, location, status))
    conn.commit()
    conn.close()
    print(f"Logged: ${offer_amount} | Time: {block_time} | Loc: {location} | Status: {status}")

if __name__ == "__main__":
    # This runs only when you execute this specific file directly
    initialize_db()
    print("Database and table verified successfully.")