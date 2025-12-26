import pandas as pd

df = pd.read_csv("data/raw/claims_raw.csv")

# Remove negative or zero claims
df = df[df["claim_amount"] > 0]

# Convert dates
df["service_date"] = pd.to_datetime(df["service_date"])

df.to_csv("data/processed/claims_fact.csv", index=False)
print("Data cleaned and saved.")
