import pandas as pd

df = pd.read_csv("data/processed/claims_fact.csv")

patient_dim = df[["patient_id", "patient_age", "gender"]].drop_duplicates()
provider_dim = df[["provider_id", "provider_type"]].drop_duplicates()
diagnosis_dim = df[["diagnosis", "diagnosis_code"]].drop_duplicates()

patient_dim.to_csv("data/processed/patient_dim.csv", index=False)
provider_dim.to_csv("data/processed/provider_dim.csv", index=False)
diagnosis_dim.to_csv("data/processed/diagnosis_dim.csv", index=False)

print("Dimensions created.")
