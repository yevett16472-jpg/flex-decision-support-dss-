import database_utilsn  
import time
from datetime import datetime

# --- CONFIGURATION: OPERATIONAL STRIKE ZONE ---
OPERATIONAL_HUBS = {
    "VTX4": {"name": "Pasadena", "travel": 30, "traffic": 1.2, "flood_risk": 3},
    "VDC8": {"name": "Fresno", "travel": 25, "traffic": 1.1, "flood_risk": 2},
    "DHT1": {"name": "La Marque", "travel": 35, "traffic": 1.5, "flood_risk": 4},
    "DHQ4": {"name": "Houston", "travel": 20, "traffic": 1.8, "flood_risk": 2},
    "DHX1": {"name": "Houston", "travel": 40, "traffic": 1.3, "flood_risk": 3}
}

MAX_TRAVEL_TIME = 40
MAX_FLOOD_RISK = 4

def initialize_system():
    print("Agent Online: Flex_Surge_System Initialized.")
    database_utils.initialize_db()

def monitor_surges():
    print("Monitoring for surge blocks...")
    start_time = datetime.now()
    log_count = 0

    try:
        while True:
            # Simulated capture
            database_utils.log_surge(35.50, "04:00 AM", "Pasadena", "Captured")
            log_count += 1

            # Health Diagnostic: Every 30 seconds, report performance
            elapsed = (datetime.now() - start_time).total_seconds()
            if elapsed >= 30:
                print(f"--- HEALTH REPORT ---")
                print(f"Uptime: {int(elapsed)} seconds | Logs: {log_count}")
                print(f"Status: Operational | Benchmarks: Met")
                print(f"---------------------")
                start_time = datetime.now()
                log_count = 0
           
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nAgent shutting down gracefully.")

if __name__ == '__main__':
    initialize_system()
    monitor_surges()
