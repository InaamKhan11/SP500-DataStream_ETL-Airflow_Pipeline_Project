# 🧠 SP500 DataStream — Automated S&P 500 ETL Pipeline using Airflow, Snowflake & AWS S3

## 📘 Project Overview
**SP500 DataStream** is an automated ETL pipeline that extracts real-time **S&P 500 stock data**, transforms it using Python, and loads the data into **AWS S3** and **Snowflake** for analytics.  
The pipeline is fully orchestrated and automated using **Apache Airflow** running inside a **Docker container**.

---

## 🏗️ Architecture Diagram
![Architecture Diagram](image/SP%20Architecture%20Diag.png)

---

## ⚙️ Project Workflow

1. **Extract**
   - Retrieves **S&P 500 symbols** from *Wikipedia*.
   - Fetches **stock price data** from *Yahoo Finance API*.

2. **Transform**
   - Cleans and formats the raw data using **Python scripts**.
   - Converts the data into a well-structured CSV format.

3. **Load**
   - Loads the transformed CSV data into:
     - **AWS S3** (as CSV backup)
     - **Snowflake Table** (for analytics and querying)

4. **Automation**
   - All ETL tasks are scheduled and managed via **Apache Airflow DAGs**.
   - The entire workflow runs automatically inside a **Docker container**.

---

##  Folder Structure
project_root/
│
├── dags/ # Airflow DAG files
├── Scripts/ # Python scripts for ETL
├── image/ # Architecture diagram and visuals
├── stock_data/ # Generated CSV files
├── stockETL.py # Main ETL script
├── .env # Environment variables (Snowflake, AWS credentials)
├── pycache/ # Compiled cache
└── README.md # Project documentation

---

##  Docker & Airflow Setup

### Start the Airflow Docker Environment
```bash
docker-compose up -d
Access Airflow Web UI
arduino
Copy code
http://localhost:8080
Trigger the DAG
Open Airflow web UI.

Click Trigger DAG.

 Technologies Used
Component	Technology
Orchestration	Apache Airflow
Data Extraction	Wikipedia, Yahoo Finance API
Data Transformation	Python (Pandas)
Data Storage	AWS S3, Snowflake
Containerization	Docker
Scheduling & Automation	Airflow DAGs

 Output
CSV Files uploaded to AWS S3.

👤 Author
Muhammad Faizan Sajid
Data Engineer
🌍 Pakistan
📧 faizansajid42@yahoo.com
💼 https://www.linkedin.com/in/muhammad-faizan-145a54269/
