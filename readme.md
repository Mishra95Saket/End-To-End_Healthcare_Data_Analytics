# Healthcare Claims Analytics – End-to-End Data Analysis Project

## Overview
This project simulates a real-world healthcare analytics use case using synthetic claims data.
The goal is to analyze cost drivers, provider performance, and patient risk patterns
commonly encountered by healthcare payers and insurance companies.

## Dataset
- Synthetic healthcare claims data generated using Python
- Modeled after CMS / insurance claims structure
- Includes patients, providers, diagnoses, and financial metrics

## Business Questions Answered
1. What are the key drivers of high healthcare costs?
2. Which providers are cost outliers compared to peers?
3. Which patients represent high utilization and financial risk?
4. How do claim costs trend over time by diagnosis category?

## Analytics Techniques
- Data cleaning & validation
- Dimensional modeling (Star Schema)
- Aggregations & KPIs
- Cost outlier detection
- Time-series trend analysis

## Tech Stack
- Python (Pandas, NumPy)
- YAML for pipeline configuration
- Matplotlib / Seaborn for visuals
- GitHub-ready modular scripts

## How to Run
```bash
pip install -r requirements.txt
python src/data_generation.py
python src/data_cleaning.py
python src/feature_engineering.py
python src/analytics.py
