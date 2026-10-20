import sqlite3
import logging
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(
    filename="surge_engine.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class SurgeDecisionEngine:
    def __init__(self, db_path: str = "pasadena_surges.db"):
        self.db_path = Path(db_path)
        self._initialize_database()

    def _initialize_database(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Pasadena_Surges (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        block_rate REAL NOT NULL,
                        surge_multiplier REAL NOT NULL,
                        is_viable INTEGER NOT NULL,
                        processed_flag INTEGER DEFAULT 0
                    )
                """)
                cursor.execute("CREATE INDEX IF NOT EXISTS idx_ts_rate ON Pasadena_Surges (timestamp, block_rate);")
                conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database initialization failed: {e}")
            raise

    def process_surge_event(self, block_rate: float, threshold: float = 35.00) -> bool:
        try:
            surge_multiplier = round(block_rate / threshold, 2)
            is_viable = 1 if block_rate >= threshold else 0
            ts = datetime.now(timezone.utc).isoformat()

            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Pasadena_Surges (timestamp, block_rate, surge_multiplier, is_viable)
                    VALUES (?, ?, ?, ?)
                """, (ts, block_rate, surge_multiplier, is_viable))
                conn.commit()
            
            logging.info(f"Processed surge block at ${block_rate}/hr. Viable: {is_viable}")
            return bool(is_viable)
        except Exception as e:
            logging.error(f"Error processing surge event (${block_rate}): {e}")
            return False

    def purge_stale_records(self, retention_days: int = 30):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM Pasadena_Surges 
                    WHERE datetime(timestamp) < datetime('now', '-' || ? || ' days')
                """, (retention_days,))
                conn.commit()
                logging.info(f"Purged records older than {retention_days} days.")
        except sqlite3.Error as e:
            logging.error(f"Purge maintenance failed: {e}")

if __name__ == "__main__":
    engine = SurgeDecisionEngine()
    engine.process_surge_event(42.50)
    print("[+] flex-decision-support-dss main_logic executed and logged successfully.")
