# 🧠 SP500 DataStream — Automated ETL Pipeline for S&P 500 Data using Airflow, Snowflake & AWS S3

## 📘 Project Overview
**SP500 DataStream** is a fully automated ETL pipeline designed to collect live **S&P 500 stock market data**, process it with Python, and store the results in **AWS S3** and **Snowflake** for advanced analytics.  
The entire workflow is orchestrated using **Apache Airflow**, running inside a **Dockerized environment** for seamless automation and portability.

---

## ⚙️ Workflow Summary

### **1. Extract**
- Pulls the latest **S&P 500 ticker list** from Wikipedia.  
- Retrieves daily stock price data directly from the **Yahoo Finance API**.

### **2. Transform**
- Cleans, validates, and structures the raw data using Python.  
- Generates standardized CSV files ready for storage and analysis.

### **3. Load**
- Uploads processed CSV files to **AWS S3** for storage and backup.  
- Inserts the transformed data into a **Snowflake table** for querying and BI workloads.

### **4. Automation**
- All tasks are scheduled, monitored, and managed through **Apache Airflow DAGs**.  
- The full ETL pipeline runs inside a **Docker container**, ensuring consistency across environments.

---

## 📂 Project Structure
project_root/
│
├── dags/ # Airflow DAG definitions
├── Scripts/ # Python ETL scripts
├── image/ # Architecture diagrams
├── stock_data/ # Generated CSV files
├── stockETL.py # Main ETL processing script
├── .env # Environment variables / credentials
├── pycache/ # Python cache
└── README.md # Documentation


---

## 🐳 Docker & Airflow Setup

### **Start Airflow in Docker**
```bash
docker-compose up -d

