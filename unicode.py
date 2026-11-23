import pandas as pd
from pathlib import Path

df = pd.read_csv(Path("data") / "customer_churn_records.csv", sep = ",")



