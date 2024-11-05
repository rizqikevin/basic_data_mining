
import pandas as pd # type: ignore
import numpy as np
import matplotlib.pyplot as plt # type: ignore

file_path = 'flower.data'
try:
    df = pd.read_csv(file_path)
    print("Data Sample:\n", df.head())
except FileNotFoundError:
    print("File tidak ditemukan. Pastikan path-nya benar.")


print("\nCek Data yang Hilang:")
print(df.isnull().sum())

print("\nDeskripsi Statistik Data:")
print(df.describe())


plt.figure(figsize=(10, 6))
plt.hist(df['sepal_length'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribusi Panjang Sepal")
plt.xlabel("Panjang Sepal (cm)")
plt.ylabel("Frekuensi")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['sepal_length'], df['sepal_width'], c='blue', alpha=0.5)
plt.title("Panjang vs Lebar Sepal")
plt.xlabel("Panjang Sepal (cm)")
plt.ylabel("Lebar Sepal (cm)")
plt.show()


avg_sepal_length = df.groupby('species')['sepal_length'].mean()
print("\nRata-rata Panjang Sepal Berdasarkan Spesies:")
print(avg_sepal_length)


avg_sepal_length.plot(kind='bar', color='coral', edgecolor='black')
plt.title("Rata-rata Panjang Sepal Berdasarkan Spesies")
plt.xlabel("Spesies")
plt.ylabel("Rata-rata Panjang Sepal (cm)")
plt.show()
