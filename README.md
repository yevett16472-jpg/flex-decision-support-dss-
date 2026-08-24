# Flex_Surge_System: Enterprise DSS

## Overview

The Flex_Surge_System is a modular, agent-led "Decision Support System" (DSS) designed to optimize logistics monitoring. By integrating autonomous data ingestion, local SQL storage, and real-time analytical processing, this system empowers users to make informed, data-driven decisions regarding surge block opportunities.

## Pandora's Box Architecture

At the heart of this project is the Pandora's Box Strategy—a 19-node logic core framework prioritizing:

* **Data Sovereignty:** Maintaining local-first workspace applications and independent database management to ensure total control over sensitive operational information.
* **Modular Node Design:** Each component of the system (Ingestion, Analysis, Visualization) operates as an independent, loosely coupled node, ensuring high maintainability and scalability.
* **Strategic Alchemy:** The integration of technical infrastructure with precise, goal-oriented business logic to manifest operational efficiency.

## Core Modules

* **setup_vault.py:** Initializes the secure SQLite "cabinet" schema.
* **surge_ingestion.py:** The autonomous engine that monitors for new surge blocks and performs initial data capture.
* **flex_db_manager.py:** The "brain" of the system; manages interactions between the ingestion nodes and the primary database.
* **surge_analysis.py:** A data processing node utilizing pandas to calculate volatility metrics and flag "reset events."
* **surge_visualizer.py:** Renders real-time trends, transforming raw data into actionable visual intelligence.

## Technical Stack

* **Language:** Python 3.14
* **Database:** SQLite3
* **Data Science:** Pandas
* **Visualization:** Matplotlib

## Structure

* **src/**: Contains all modular source code for ingestion, analysis, and visualization engines.