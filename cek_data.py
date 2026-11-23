import pandas as pd
from pathlib import Path

df = pd.read_csv(Path("data") / "customer_churn_records.csv", sep = ",")
print(df.shape) #(10000, 10)

print(df.head())

# Cek kesehatan data (kosong dan hilang)
print(df.isna().sum())
df.info()

# Cek duplikat
print("Jumlah data duplikat: ", df.duplicated().sum()) # 0

# Penulisan
print(df["Geography"].value_counts())
print(df["Gender"].value_counts())
print(df["NumOfProducts"].value_counts())

# Cek kolom dengan tipe float atau int
print(df[["RowNumber", "CustomerId", "Balance", "CreditScore", "Age", "Tenure", "NumOfProducts"]].describe())

# Cek apakah penamaan kolom konsisten
print(df["Surname"].str.strip().nunique()) # 2932
print(df["Geography"].str.strip().nunique()) # 3 (France, Germany, Spain)
print(df["Gender"].str.strip().nunique()) # 2 (Male, Female)

# Cek apakah pada kolom SUrname huruf depannya sudah kapital semua
print(df["Surname"].str[0].str.istitle().sum())

# Cek nilai minimum dan maksimum semua kolom numerik
print(df.describe().T[["min", "50%", "max"]])

# Cek apakah jumlah Customer ID sama dengan total baris
print(df["CustomerId"].nunique() == len(df)) # True (Tidak ada sel kosong)

# Cek nama marga yang mengandung karakter selain huruf, spasi, '
cek_surname = df[df["Surname"].str.contains(r"[^a-zA-Z\s'-]", na=False)]

print("Daftar marga yang mengandung tanda tanya: ", cek_surname["Surname"].unique())

# Cek banyak baris yang mengandung marga yg sama
print("Jumlah baris dengan nilai L?:", (df["Surname"] == "L?").sum())
print("Jumlah baris dengan nilai H?:", (df["Surname"] == "H?").sum())
print("Jumlah baris dengan nilai Hs?:", (df["Surname"] == "Hs?").sum())
print("Jumlah baris dengan nilai Y?An:", (df["Surname"] == "Y?An").sum())
print("Jumlah baris dengan nilai K?:", (df["Surname"] == "K?").sum())
print("Jumlah baris dengan nilai Y?:", (df["Surname"] == "Y?").sum())
print("Jumlah baris dengan nilai Hs?Eh:", (df["Surname"] == "Hs?Eh").sum())

print("\nTotal baris yang terdampak:", len(cek_surname))

# Nama-nama di atas sudah ada di dalam dataset asli sehingga bukan kesalahan encoding python
# Nama dibiarkan karena tidak terlalu berpengaruh terhadap analisis