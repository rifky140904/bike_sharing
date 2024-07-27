# Rifky Collection Dashboard

## Setup Environment - Windows Command Prompt

1. Buat direktori proyek dan masuk ke dalamnya:

   ```cmd
   mkdir proyek_analisis_data
   cd proyek_analisis_data
   ```

2. Buat dan aktifkan lingkungan virtual menggunakan `virtualenv` atau `venv`:

   ```cmd
   # Menggunakan virtualenv
   pip install virtualenv
   virtualenv env
   env\Scripts\activate  # Aktifkan lingkungan virtual

   # Atau, menggunakan venv (Python 3.3+)
   python -m venv env
   env\Scripts\activate  # Aktifkan lingkungan virtual
   ```

3. Instal semua dependensi yang diperlukan:
   ```cmd
   pip install -r requirements.txt
   ```

## Run Streamlit App

1. Jalankan aplikasi Streamlit dengan perintah berikut:
   ```cmd
   streamlit run dashboard.py
   ```

## Catatan Tambahan

- Pastikan Anda memiliki file `requirements.txt` yang berisi semua paket yang diperlukan untuk proyek ini.
- Jika Anda mengalami masalah terkait dependensi, pastikan untuk menginstal ulang atau memperbarui paket yang bermasalah.
