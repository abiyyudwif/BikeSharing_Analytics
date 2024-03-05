# Import packages
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Set page title and sidebar header
st.title("Dashboard Penyewaan Sepeda")
st.sidebar.header("Pilih Konten")

# Create a selectbox widget for content selection
content = st.sidebar.selectbox("Konten", ["1. Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan", "2. Korelasi positif antara temperatur dan jumlah pengguna sepeda pada musim panas (Juni - Agustus) di tahun 2011", "3. Perkembangan jumlah penyewaan sepeda dari bulan ke bulan", "4. Korelasi antara suhu dan jumlah penyewaan sepeda pada hari-hari kerja dan hari-hari libur", "5. Tren keseluruhan jumlah penyewaan sepeda selama periode yang diamati"])

# Display the selected content
if content == "1. Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan":
    # Calculate the mean of cnt by workingday
    mean_cnt = df_day.groupby("workingday")["cnt"].mean()
    # Calculate the percentage difference
    diff = (mean_cnt[1] - mean_cnt[0]) / mean_cnt[0] * 100
    # Display the result
    st.write(f"Rata-rata jumlah pengguna sepeda pada hari kerja adalah {mean_cnt[1]:.2f}")
    st.write(f"Rata-rata jumlah pengguna sepeda pada akhir pekan adalah {mean_cnt[0]:.2f}")
    st.write(f"Perbedaan rata-rata jumlah pengguna sepeda pada hari kerja dan akhir pekan adalah {diff:.2f}%")
elif content == "2. Korelasi positif antara temperatur dan jumlah pengguna sepeda pada musim panas (Juni - Agustus) di tahun 2011":
    # Filter the data by year and month
    df_2011_summer = df_day[(df_day["yr"] == 0) & (df_day["mnth"].isin([6, 7, 8]))]
    # Calculate the correlation coefficient
    corr = df_2011_summer["temp"].corr(df_2011_summer["cnt"])
    # Display the result
    st.write(f"Koefisien korelasi antara temperatur dan jumlah pengguna sepeda pada musim panas di tahun 2011 adalah {corr:.2f}")
    # Plot a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df_2011_summer["temp"], df_2011_summer["cnt"])
    ax.set_xlabel("Temperatur")
    ax.set_ylabel("Jumlah Pengguna Sepeda")
    ax.set_title("Scatter Plot Temperatur vs Jumlah Pengguna Sepeda pada Musim Panas di Tahun 2011")
    st.pyplot(fig)
elif content == "3. Perkembangan jumlah penyewaan sepeda dari bulan ke bulan":
    # Calculate the mean of cnt by month
    mean_cnt_month = df_day.groupby("mnth")["cnt"].mean()
    # Display the result
    st.write("Rata-rata jumlah penyewaan sepeda dari bulan ke bulan adalah:")
    st.write(mean_cnt_month)
    # Plot a line plot
    fig, ax = plt.subplots()
    ax.plot(mean_cnt_month.index, mean_cnt_month.values)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Rata-Rata Jumlah Penyewaan Sepeda")
    ax.set_title("Line Plot Rata-Rata Jumlah Penyewaan Sepeda dari Bulan ke Bulan")
    st.pyplot(fig)
elif content == "4. Korelasi antara suhu dan jumlah penyewaan sepeda pada hari-hari kerja dan hari-hari libur":
    # Calculate the correlation coefficient by workingday
    corr_work = df_day[df_day["workingday"] == 1]["temp"].corr(df_day[df_day["workingday"] == 1]["cnt"])
    corr_holi = df_day[df_day["workingday"] == 0]["temp"].corr(df_day[df_day["workingday"] == 0]["cnt"])
    # Display the result
    st.write(f"Koefisien korelasi antara suhu dan jumlah penyewaan sepeda pada hari kerja adalah {corr_work:.2f}")
    st.write(f"Koefisien korelasi antara suhu dan jumlah penyewaan sepeda pada hari libur adalah {corr_holi:.2f}")
    # Plot a scatter plot by workingday
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].scatter(df_day[df_day["workingday"] == 1]["temp"], df_day[df_day["workingday"] == 1]["cnt"])
    ax[0].set_xlabel("Temperatur")
    ax[0].set_ylabel("Jumlah Pengguna Sepeda")
    ax[0].set_title("Scatter Plot Temperatur vs Jumlah Pengguna Sepeda pada Hari Kerja")
    ax[1].scatter(df_day[df_day["workingday"] == 0]["temp"], df_day[df_day["workingday"] == 0]["cnt"])
    ax[1].set_xlabel("Temperatur")
    ax[1].set_ylabel("Jumlah Pengguna Sepeda")
    ax[1].set_title("Scatter Plot Temperatur vs Jumlah Pengguna Sepeda pada Hari Libur")
    st.pyplot(fig)
else: # content == "5. Tren keseluruhan jumlah penyewaan sepeda selama periode yang diamati":
    # Display the result
    st.write("Tren keseluruhan jumlah penyewaan sepeda selama periode yang diamati adalah:")
    st.write(df_day["cnt"].describe())
    # Plot a line plot
    fig, ax = plt.subplots()
    ax.plot(df_day["dteday"], df_day["cnt"])
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_title("Line Plot Jumlah Penyewaan Sepeda dari Tanggal ke Tanggal")
    st.pyplot(fig)
