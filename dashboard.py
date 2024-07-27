import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
hour_df = pd.read_csv('hour.csv')
day_df = pd.read_csv('day.csv')

# Convert 'dteday' to datetime format
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Streamlit app
st.title('Dashboard Analisis Bike Sharing')

# Sidebar for selecting data view
st.sidebar.title('Menu Analisis')
option = st.sidebar.selectbox(
    'Pilih Jenis Analisis:',
    ['Pengaruh Cuaca dan Musim', 'Tren Penggunaan Sepeda']
)

if option == 'Pengaruh Cuaca dan Musim':
    st.header('Pengaruh Cuaca dan Musim terhadap Jumlah Penyewaan')

    # Scatter plot suhu vs. jumlah penyewaan
    st.subheader('Pengaruh Suhu terhadap Jumlah Penyewaan')
    fig, ax = plt.subplots()
    sns.scatterplot(x='temp', y='cnt', data=hour_df, alpha=0.3, ax=ax)
    ax.set_title('Suhu vs. Jumlah Penyewaan')
    ax.set_xlabel('Suhu (ternormalisasi)')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

    # Box plot jumlah penyewaan berdasarkan musim (hourly data)
    st.subheader('Jumlah Penyewaan Berdasarkan Musim (Data Jam)')
    fig, ax = plt.subplots()
    sns.boxplot(x='season', y='cnt', data=hour_df, ax=ax)
    ax.set_title('Jumlah Penyewaan Berdasarkan Musim (Data Jam)')
    ax.set_xlabel('Musim (1=Spring, 2=Summer, 3=Fall, 4=Winter)')
    ax.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig)

    # Box plot jumlah penyewaan berdasarkan musim (daily data)
    st.subheader('Jumlah Penyewaan Berdasarkan Musim (Data Harian)')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=day_df, ax=ax)
    ax.set_title('Jumlah Penyewaan Berdasarkan Musim (Data Harian)')
    ax.set_xlabel('Musim (1=Spring, 2=Summer, 3=Fall, 4=Winter)')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.grid(True)
    st.pyplot(fig)

elif option == 'Tren Penggunaan Sepeda':
    st.header('Tren Penggunaan Sepeda')

    # Plot jumlah penyewaan berdasarkan jam
    st.subheader('Rata-rata Jumlah Penyewaan Berdasarkan Jam')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='hr', y='cnt', data=hour_df.groupby(
        'hr')['cnt'].mean().reset_index(), ax=ax)
    ax.set_title('Rata-rata Jumlah Penyewaan Berdasarkan Jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan')
    ax.grid(True)
    st.pyplot(fig)

    # Plot jumlah penyewaan berdasarkan hari dalam seminggu
    st.subheader('Rata-rata Jumlah Penyewaan Berdasarkan Hari dalam Seminggu')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='weekday', y='cnt', data=hour_df.groupby(
        'weekday')['cnt'].mean().reset_index(), ax=ax)
    ax.set_title('Rata-rata Jumlah Penyewaan Berdasarkan Hari dalam Seminggu')
    ax.set_xlabel('Hari dalam Seminggu (0=Senin, 6=Minggu)')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan')
    ax.grid(True)
    st.pyplot(fig)

    # Plot jumlah penyewaan berdasarkan bulan
    st.subheader('Rata-rata Jumlah Penyewaan Berdasarkan Bulan')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='mnth', y='cnt', data=hour_df.groupby(
        'mnth')['cnt'].mean().reset_index(), ax=ax)
    ax.set_title('Rata-rata Jumlah Penyewaan Berdasarkan Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata Jumlah Penyewaan')
    ax.grid(True)
    st.pyplot(fig)

    # Plot tren penggunaan sepeda selama dua tahun
    st.subheader('Tren Jumlah Penyewaan Harian')
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='dteday', y='cnt', data=day_df, ax=ax)
    ax.set_title('Tren Jumlah Penyewaan Harian')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.grid(True)
    st.pyplot(fig)
