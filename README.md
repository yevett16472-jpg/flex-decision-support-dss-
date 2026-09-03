# flex-decision-support-dss

A secure, local decision support system designed to monitor, analyze, and log Amazon Flex surge blocks for the Pasadena market. This repository operates strictly as a human-in-the-loop tool to assist with data tracking and operational awareness.

---

## Architecture & Overview

The system acts as a local data processing pipeline that captures surge data feeds, processes metrics through Python scripts, and logs historical trends into a structured SQL database.

* **Human-in-the-Loop Design**: Functions strictly as an intelligence and decision support dashboard; all final selections and scheduling actions remain under manual control.
* **Data Privacy & Storage**: Keeps all tracking logs isolated locally or within secure private architectures to preserve operational sovereignty.

---

## Database Initialization

The backend relies on local SQL tables to track surge history. Deploy the required schema before running monitoring scripts.

1. Access your local SQL environment.
2. Execute the schema script to provision the `Pasadena_Surges` tracking table:
   ```sql
   CREATE TABLE Pasadena_Surges (
       surge_id INT AUTO_INCREMENT PRIMARY KEY,
       timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
       block_time VARCHAR(50),
       payout DECIMAL(10, 2),
       station_location VARCHAR(100),
       status VARCHAR(50)
   );
