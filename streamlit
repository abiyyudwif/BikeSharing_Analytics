import streamlit as st
import pandas as pd
import plotly.express as px

# Membaca data
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Title
st.title('Dashboard Analisis Data Sepeda')

# EDA
st.header('Exploratory Data Analysis (EDA)')

# Statistik Deskriptif
st.subheader('Statistik Deskriptif')
st.write(df_day.describe())

# Visualisasi Distribusi Variabel
st.subheader('Visualisasi Distribusi Variabel')
fig = px.histogram(df_day, x='cnt', nbins=50, title='Distribusi Jumlah Pengguna Sepeda')
st.plotly_chart(fig)

# Analisis Korelasi
st.subheader('Analisis Korelasi')
correlation = df_day[['temp', 'cnt']].corr().iloc[0, 1]
st.write(f"Korelasi antara temperatur dan jumlah pengguna sepeda: {correlation}")

# Analisis Tren
st.subheader('Analisis Tren')
fig_trend = px.line(df_day, x='dteday', y='cnt', title='Tren Jumlah Pengguna Sepeda')
st.plotly_chart(fig_trend)

# Analisis Variabel Kategorikal
st.subheader('Analisis Variabel Kategorikal')
fig_season = px.bar(df_day, x='season', y='cnt', title='Jumlah Pengguna Sepeda berdasarkan Musim')
st.plotly_chart(fig_season)

# Jawab Pertanyaan
st.header('Jawaban Pertanyaan')
# Pertanyaan 1
avg_cnt_workingday = df_day.groupby('workingday')['cnt'].mean()
diff_percentage = ((avg_cnt_workingday[1] - avg_cnt_workingday[0]) / avg_cnt_workingday[0]) * 100
st.write(f"Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan: {diff_percentage:.2f}%")

# Pertanyaan 2
summer_2011 = df_day[(df_day['yr'] == 0) & (df_day['mnth'].isin([6, 7, 8]))]
correlation_temp_cnt = summer_2011[['temp', 'cnt']].corr().iloc[0, 1]
st.write(f"Korelasi antara temperatur dan jumlah pengguna sepeda pada musim panas di tahun 2011: {correlation_temp_cnt}")

