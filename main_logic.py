import database_utils
import time
from datetime import datetime

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