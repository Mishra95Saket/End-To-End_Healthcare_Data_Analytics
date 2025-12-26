import pandas as pd

df = pd.read_csv("data/processed/claims_fact.csv")

# 1. Cost drivers
cost_by_diag = df.groupby("diagnosis")["claim_amount"].mean().sort_values(ascending=False)
print("\nAvg Cost by Diagnosis:\n", cost_by_diag)

# 2. Provider outliers
provider_cost = df.groupby("provider_id")["claim_amount"].mean()
outliers = provider_cost[provider_cost > provider_cost.quantile(0.95)]
print("\nHigh Cost Providers:\n", outliers.head())

# 3. High-risk patients
patient_risk = df.groupby("patient_id").agg(
    total_cost=("claim_amount", "sum"),
    claim_count=("claim_id", "count")
)
high_risk = patient_risk[(patient_risk.total_cost > 50000) & (patient_risk.claim_count > 5)]
print("\nHigh Risk Patients:\n", high_risk.head())

# 4. Trend analysis
df["month"] = pd.to_datetime(df["service_date"]).dt.to_period("M")
trend = df.groupby(["month", "diagnosis"])["claim_amount"].sum()
print("\nMonthly Cost Trends:\n", trend.head())
