import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

NUM_RECORDS = 50000

diagnosis_codes = {
    "Diabetes": "E11",
    "Hypertension": "I10",
    "Heart Disease": "I25",
    "Cancer": "C50",
    "Asthma": "J45"
}

provider_types = ["Hospital", "Clinic", "Specialist"]

data = []

for i in range(NUM_RECORDS):
    claim_amount = np.round(np.random.gamma(2, 3000), 2)
    data.append({
        "claim_id": f"CLM{i+1}",
        "patient_id": f"PAT{random.randint(1000, 5000)}",
        "provider_id": f"PRV{random.randint(100, 500)}",
        "provider_type": random.choice(provider_types),
        "diagnosis": random.choice(list(diagnosis_codes.keys())),
        "diagnosis_code": diagnosis_codes[random.choice(list(diagnosis_codes.keys()))],
        "claim_amount": claim_amount,
        "service_date": fake.date_between(start_date="-2y", end_date="today"),
        "patient_age": random.randint(18, 85),
        "gender": random.choice(["M", "F"])
    })

df = pd.DataFrame(data)
df.to_csv("data/raw/claims_raw.csv", index=False)
print("Synthetic claims data generated.")
