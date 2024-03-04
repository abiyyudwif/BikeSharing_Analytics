import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Mematikan warning yang tidak perlu
st.set_option('deprecation.showPyplotGlobalUse', False)
warnings.filterwarnings('ignore')

# Membaca data
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Fungsi untuk menganalisis data dan membuat visualisasi
def analyze_data():
    # Menampilkan statistik deskriptif
    st.subheader("Statistik Deskriptif")
    st.write(df_day.describe())

    # Visualisasi Distribusi Variabel
    st.subheader("Visualisasi Distribusi Variabel")
    numerical_features = ['temp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
    for feature in numerical_features:
        plt.figure(figsize=(8, 6))
        sns.histplot(df_day[feature], kde=True)
        plt.title(f'Distribusi {feature}')
        st.pyplot()

    # Analisis Korelasi
    st.subheader("Analisis Korelasi")
    summer_data = df_day[(df_day['yr'] == 0) & (df_day['mnth'].isin([6, 7, 8])) & (df_day['season'] == 2)]
    correlation = summer_data[['temp', 'cnt']].corr()['cnt'][0]
    st.write(f"Korelasi antara temperatur dan jumlah pengguna sepeda pada musim panas tahun 2011: {correlation}")

    # Analisis Tren
    st.subheader("Analisis Tren")
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_day, x='dteday', y='cnt', hue='yr')
    plt.title('Tren Jumlah Pengguna Sepeda dari Tahun ke Tahun')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Pengguna Sepeda')
    plt.xticks(rotation=45)
    st.pyplot()

    # Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan
    st.subheader("Perbedaan Rata-rata Pengguna Sepeda pada Hari Kerja dan Akhir Pekan")
    weekday_avg = df_day[df_day['workingday'] == 1]['cnt'].mean()
    weekend_avg = df_day[df_day['workingday'] == 0]['cnt'].mean()
    difference = (weekend_avg - weekday_avg) / weekday_avg * 100
    st.write(f"Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan: {difference:.2f}%")

# Menjalankan fungsi untuk menganalisis data
analyze_data()
