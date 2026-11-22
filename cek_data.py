import pandas as pd

df = pd.read_csv("customer_churn_records.csv", sep = ",")
print(df.shape) #(10000, 10)

print(df.head())

# Cek kesehatan data (kosong, duplikat, konsistensi penulisan, data hilang)
print(df.isna().sum())
df.info()

# Cek duplikat
print("Jumlah data duplikat: ", df.duplicated().sum()) # 0

# Penulisan (tidak ada nilai yg negatif dan duplikat)
print(df["Geography"].value_counts())
print(df["Gender"].value_counts())
print(df["NumOfProducts"].value_counts())

# Cek kolom dengan tipe float atau int
print(df[["RowNumber", "CustomerId", "Balance", "CreditScore", "Age", "Tenure", "NumOfProducts"]].describe())

# Cek spasi berlebih
print(df["Surname"].str.strip().nunique()) # 2932
print(df["Geography"].str.strip().nunique()) # 3
print(df["Gender"].str.strip().nunique()) # 2

# Hapus spasi berlebih dan capitalize
df["Surname"] = df["Surname"].str.strip().str.title()
df["Geography"] = df["Geography"].str.strip().str.title()
df["Gender"] = df["Gender"].str.strip().str.title()

# Cek nilai minimum dan maksimum semua kolom numerik
print(df.describe().T[["min", "50%", "max"]])

# Cek apakah jumlah Customer ID sama dengan total baris
print(df["CustomerId"].nunique() == len(df))

# Cek Customer dengan ID sama
print(df[df.duplicated("CustomerId", keep=False)])

# Cek nama marga yang mengandung karakter selain huruf, spasi, '
cek_surname = df[df["Surname"].str.contains(r"[^a-zA-Z\s'-]", na=False)]

print("Daftar nama unik yang aneh:")
print(cek_surname["Surname"].unique())

# Cek banyak baris yang mengandung marga yg sama
print("Jumlah baris dengan nilai L?:", (df["Surname"] == "L?").sum())
print("Jumlah baris dengan nilai H?:", (df["Surname"] == "H?").sum())
print("Jumlah baris dengan nilai Hs?:", (df["Surname"] == "Hs?").sum())
print("Jumlah baris dengan nilai Y?An:", (df["Surname"] == "Y?An").sum())
print("Jumlah baris dengan nilai K?:", (df["Surname"] == "K?").sum())
print("Jumlah baris dengan nilai Y?:", (df["Surname"] == "Y?").sum())
print("Jumlah baris dengan nilai Hs?Eh:", (df["Surname"] == "Hs?Eh").sum())

print("\nTotal baris yang terdampak:", len(cek_surname))

# Menghapus karakter tanda tanya (?)
df["Surname"] = df["Surname"].str.replace("?", "", regex=False)

# Cek ulang
cek_surname = df[df["Surname"].str.contains(r"[^a-zA-Z\s'-]", na=False)]

print("Daftar nama unik yang aneh:")
print(cek_surname["Surname"].unique())