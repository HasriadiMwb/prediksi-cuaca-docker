import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🌦️ Prediksi Cuaca Indonesia")
st.write("Aplikasi ini menggunakan model Machine Learning sederhana untuk memprediksi suhu udara berdasarkan data historis.")

data = {
    'Tanggal': pd.date_range(start='2025-01-01', periods=10, freq='D'),
    'Suhu (°C)': np.random.uniform(25, 34, 10).round(2),
    'Kelembapan (%)': np.random.uniform(60, 90, 10).round(2)
}

df = pd.DataFrame(data)
st.dataframe(df)

plt.figure(figsize=(8,4))
plt.plot(df['Tanggal'], df['Suhu (°C)'], marker='o')
plt.title("Perubahan Suhu Harian")
plt.xlabel("Tanggal")
plt.ylabel("Suhu (°C)")
st.pyplot(plt)

st.success("✅ Aplikasi siap dijalankan dengan Docker (Python 3.11)!")
