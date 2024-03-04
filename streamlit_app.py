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
def analyze_data(df):
    # Sidebar untuk menampilkan informasi
    st.sidebar.subheader("Informasi")
    st.sidebar.write("Dashboard ini menyediakan analisis data sepeda.")
    st.sidebar.write("Anda dapat melihat perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan, serta korelasi antara temperatur dan jumlah pengguna sepeda pada musim panas tahun 2011.")

    # Judul Dashboard
    st.title("Dashboard Analisis Data Sepeda")

    # Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan
    st.subheader("Perbedaan Rata-rata Pengguna Sepeda pada Hari Kerja dan Akhir Pekan")
    weekday_avg = df[df['workingday'] == 1]['cnt'].mean()
    weekend_avg = df[df['workingday'] == 0]['cnt'].mean()
    difference = (weekend_avg - weekday_avg) / weekday_avg * 100
    st.write(f"Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan: {difference:.2f}%")

    # Analisis Korelasi antara Temperatur dan Jumlah Pengguna Sepeda pada Musim Panas 2011
    st.subheader("Analisis Korelasi antara Temperatur dan Jumlah Pengguna Sepeda pada Musim Panas 2011")
    summer_data = df[(df['yr'] == 0) & (df['mnth'].isin([6, 7, 8])) & (df['season'] == 2)]
    correlation = summer_data[['temp', 'cnt']].corr()['cnt'][0]
    st.write(f"Korelasi antara temperatur dan jumlah pengguna sepeda pada musim panas tahun 2011: {correlation}")

    # Statistik Deskriptif
    st.subheader("Statistik Deskriptif")
    st.write(df.describe())

    # Visualisasi Distribusi Variabel
    st.subheader("Visualisasi Distribusi Variabel")
    numerical_features = ['temp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
    for feature in numerical_features:
        st.write(f"### Distribusi {feature}")
        if feature in ['temp', 'hum', 'windspeed']:
            fig, ax = plt.subplots()
            sns.histplot(df[feature], kde=True, ax=ax)
            ax.set_title(f'Distribusi {feature}')
            st.pyplot(fig)
        elif feature in ['casual', 'registered', 'cnt']:
            fig, ax = plt.subplots()
            sns.histplot(df[feature], kde=True, ax=ax)
            ax.set_title(f'Distribusi {feature.capitalize()}')
            st.pyplot(fig)

    # Analisis Tren
    st.subheader("Analisis Tren")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=df, x='dteday', y='cnt', ax=ax)
    ax.set_title('Tren Jumlah Pengguna Sepeda')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Pengguna Sepeda')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Analisis Variabel Kategorikal
    st.subheader("Analisis Variabel Kategorikal")
    categorical_features = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']
    for feature in categorical_features:
        st.write(f"### Distribusi {feature}")
        st.write(df[feature].value_counts())

# Menjalankan fungsi untuk menganalisis data
analyze_data(df_day)
