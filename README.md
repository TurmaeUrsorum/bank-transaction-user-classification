# bank transaction user classification

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)
![NumPy](https://img.shields.io/badge/numpy-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EB5E28?logo=xgboost&logoColor=white)
![Matplotlib](https://img.shields.io/badge/matplotlib-11557C?logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/seaborn-4C72B0)

![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)


## Deskripsi

Penjelasan komprehensif tentang projek data science ini. 
### **Masalah Bisnis**
Bank memiliki jumlah nasabah yang besar dengan pola transaksi yang sangat beragam. Tanpa pemahaman mendalam tentang perilaku transaksi, sulit untuk

* Mengidentifikasi segmen nasabah yang berbeda.
* Menawarkan produk yang tepat.
* Mengurangi risiko churn (nasabah berhenti menggunakan layanan).
* Meningkatkan efektivitas pemasaran dan manajemen risiko.
  
### **Tujuan Utama**
Mengelompokkan nasabah berdasarkan pola transaksi mereka (misalnya frekuensi transaksi, jenis transaksi, nominal, merchant, dsb.) menggunakan algoritma classification agar bank memahami karakteristik masing-masing segmen yang telah di hasilkan dari model clustering.

### **Nilai tambah**
Hasil dari klasifikasi dapat digunakan untuk
* **Personalisasi produk finansial** → misal kartu kredit, deposito, pinjaman, atau investment product.
* **Efisiensi pemasaran** → kampanye bisa ditargetkan ke segmen tertentu.
* **Mengenali nasabah berisiko tinggi** → deteksi fraud atau transaksi tidak wajar lebih cepat.
* **Meningkatkan retensi** → strategi mempertahankan nasabah disesuaikan berdasarkan perilaku.
* **Mendukung keputusan bisnis** → manajemen bisa melihat komposisi nasabah secara real-time.

### **Target audience**
* **Tim Data & Analytics** → untuk membuat model dan insight.
* **Tim Marketing** → untuk menjalankan kampanye yang lebih tepat sasaran.
* **Tim Product Banking** → mendesain produk sesuai kebutuhan segmen.
* **Manajemen Bank** → bahan pengambilan keputusan.
* (Opsional) **Tim Risk/Fraud** → memahami perilaku mencurigakan berdasarkan cluster.

## Business Understanding

### Problem Statement
Bank memiliki data transaksi nasabah yang sangat besar dan beragam, namun belum dimanfaatkan secara optimal untuk memahami perilaku dan kebutuhan nasabah. Akibatnya, bank kesulitan menentukan strategi pemasaran yang tepat, menawarkan produk yang relevan, serta mengidentifikasi kelompok nasabah yang berisiko tinggi atau berpotensi churn. Diperlukan sebuah model yang mampu mengelompokkan nasabah berdasarkan pola transaksi mereka sehingga bank dapat mengambil keputusan lebih cepat, tepat, dan berbasis data.
