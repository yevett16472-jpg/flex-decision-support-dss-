import sqlite3
import pandas as pd

class FlexDBManager:
    def __init__(self, db_name="flex_system.db"):
        self.db_name = db_name
        self._initialize_table()

    def _initialize_table(self):
        """Ensures the Pasadena_Surges table exists."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Pasadena_Surges (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    offer_amount REAL,
                    surge_multiplier REAL,
                    status TEXT
                )
            ''')
            conn.commit()

    def get_connection(self):
        """Returns a connection to the database."""
        return sqlite3.connect(self.db_name)

    def read_sql_query(self, query):
        """Reads data into a Pandas DataFrame."""
        try:
            with self.get_connection() as conn:
                return pd.read_sql_query(query, conn)
        except Exception as e:
            print(f"Error querying table: {e}")
            return pd.DataFrame()

    def log_surge(self, offer_amount, surge_multiplier, status="active"):
        """Inserts a new record into the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO Pasadena_Surges (offer_amount, surge_multiplier, status)
                    VALUES (?, ?, ?)
                ''', (offer_amount, surge_multiplier, status))
                conn.commit()
        except Exception as e:
            print(f"Error logging surge: {e}")

# Verification block
if __name__ == "__main__":
    db = FlexDBManager()
    print("flex_db_manager.py successfully loaded and database structure verified.")