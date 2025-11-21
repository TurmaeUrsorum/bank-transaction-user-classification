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


## **📖 Deskripsi**
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

## **🎯 Business Understanding**

### **Problem Statement**
Bank memiliki data transaksi nasabah yang sangat besar dan beragam, namun belum dimanfaatkan secara optimal untuk memahami perilaku dan kebutuhan nasabah. Akibatnya, bank kesulitan menentukan strategi pemasaran yang tepat, menawarkan produk yang relevan, serta mengidentifikasi kelompok nasabah yang berisiko tinggi atau berpotensi churn. Diperlukan sebuah model yang mampu mengelompokkan nasabah berdasarkan pola transaksi mereka sehingga bank dapat mengambil keputusan lebih cepat, tepat, dan berbasis data.

### **Objectives**

* [ ] **Tujuan 1:** Menghasilkan label nasabah menggunakan model clustering (misalnya K-Means) untuk membentuk segmentasi awal berdasarkan pola transaksi.
* [ ] **Tujuan 2:** Membangun model classification yang mampu memprediksi kelas/segmen nasabah baru berdasarkan fitur transaksi mereka dengan akurasi yang stabil.
* [ ] **Tujuan 3:** Mengidentifikasi fitur-fitur transaksi yang paling berpengaruh dalam menentukan kelas/segmen nasabah.
* [ ] **Tujuan 4:** Menyediakan dashboard atau visualisasi untuk memonitor distribusi kelas, performa model, serta perubahan perilaku nasabah dari waktu ke waktu.

### **Success Metrics**

#### **Bisnis Metrics**
##### **1. Peningkatan efektivitas targeting**

* Meningkatkan response rate kampanye berdasarkan segmen minimal **> 10%**.
* Atau peningkatan konversi produk per segmen minimal **> 8%**.

##### **2. Efisiensi biaya marketing**

* Pengurangan biaya promosi karena targeting lebih tepat → **> 15%** efisiensi.

##### **3. Peningkatan engagement**

* Frekuensi transaksi naik **> 5%** untuk segmen tertentu.
* Atau peningkatan saldo rata-rata pada segmen high-value.

##### **4. Peningkatan akurasi segmentasi operasional**

* Tim marketing atau risk bisa mengidentifikasi segmen dengan benar minimal **> 90%** berdasarkan rule cluster.

## **🗂️ Dataset**
### **Sumber Dataset**
 **Primary Source**: [Bank Transaction Dataset](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)

### Dataset Overview
```python
Shape: (2512, 16)
Missing Values: 0%
Duplicate Rows: 0%
```

### **Dataset Description**
| Feature                 | Type    | Description                              | Missing Values |
| ----------------------- | ------- | ---------------------------------------- | -------------- |
| TransactionID           | object  | ID unik transaksi                        | 0%             |
| AccountID               | object  | ID nasabah                               | 0%             |
| TransactionAmount       | float64 | Nominal transaksi                        | 0%             |
| TransactionDate         | object  | Tanggal transaksi                        | 0%             |
| TransactionType         | object  | Jenis transaksi (misal: debit/kredit)    | 0%             |
| Location                | object  | Lokasi transaksi                         | 0%             |
| DeviceID                | object  | ID perangkat yang digunakan              | 0%             |
| IP Address              | object  | Alamat IP saat transaksi                 | 0%             |
| MerchantID              | object  | ID merchant                              | 0%             |
| Channel                 | object  | Kanal transaksi (ATM, mobile, web, dll.) | 0%             |
| CustomerAge             | int64   | Usia nasabah                             | 0%             |
| CustomerOccupation      | object  | Pekerjaan nasabah                        | 0%             |
| TransactionDuration     | int64   | Durasi proses transaksi                  | 0%             |
| LoginAttempts           | int64   | Jumlah percobaan login sebelum transaksi | 0%             |
| AccountBalance          | float64 | Saldo rekening saat transaksi            | 0%             |
| PreviousTransactionDate | object  | Tanggal transaksi sebelumnya             | 0%             |
| Cluster                 | int64   | Label cluster hasil unsupervised model   | 0%             |


## 🏗️ Struktur Projek
```
data_science_project/
├── conf/                          # Configuration data catalog
│   ├── base/                      # Base configuration
│   │   ├── catalog.yml
│   │   ├── parameters_data_EDA.yml
│   │   └── parameters_model_training.yml
│   ├── dev/                       # Development configuration
│   │   ├── catalog.yml
│   │   ├── parameters_data_EDA.yml
│   │   └── parameters_model_training.yml
│   └── prod/                      # Production configuration
│       ├── catalog.yml
│       ├── parameters_data_EDA.yml
│       └── parameters_model_training.yml
├── data/                          # Data storage
│   ├── 01_raw/                    # data asli atau mentah
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── external_data.csv
│   ├── 02_Intermediate/           # data yang sudah clean
│   │   ├── train_cleaned.csv
│   │   ├── test_cleaned.csv
│   │   └── feature_engineered.csv
│   ├── 03_primary/                # data yang sudah siap untuk preproses
│   └── 04_feature/                # data yang dihasilkan dari feature engineering
|   └── 05_model_input/            # data yang siap untuk model training
│
├── docs/                          # Documentation
|
├── models/                        # Model storage
|                      
├── notebooks/                     # Jupyter notebooks
│   ├── 01_eda.ipynb               # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_interpretation.ipynb
│
├── reports/                       # Report storage
│
├── src/
│   ├── project_name/
│   │   ├── __init__.py
│   │   ├── pipelines/
│   │   │   ├── data_cleaning/     # pipeline data cleaning/
│   │   │   │   ├── nodes.py       # preprocess, cleaning
│   │   │   │   └── pipeline.py
│   │   │   ├── data_EDA/
│   │   │   │   ├── nodes.py       # EDA, feature engineering
│   │   │   │   └── pipeline.py
│   │   │   ├── data_evaluation/
│   │   │   │   ├── nodes.py       # model evaluation
│   │   │   │   └── pipeline.py
│   │   │   └── data_modeling/
│   │   │   |   ├── nodes.py       # model training
│   │   │   |   └── pipeline.py
│   │   │   └── data_preproses/
│   │   │       ├── nodes.py       # data preproses
│   │   │       └── pipeline.py
│   │   │
│   │   ├── __main__.py            # Project entry point
│   │   └── pipeline_registry.py   # Pipeline registry
│   │   └── setings.py             # Project settings
│   │  
│   │   
│   │       
│   │       
│   │       
│   │
│   └── setup.py                   # Project metadata
│
├── tests/                         # Unit tests
│   ├── pipelines/
|   │   ├── data_cleaning/
│   │   ├── data_EDA/
│   │   ├── data_evaluation/
│   │   ├── data_modeling/
│   │   └── data_preproses/
│   ├── conftest.py
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   └── test_models.py
│
├── environment.yml                # Conda environment
├── pyproject.toml                 # Project configuration
├── setup.py                       # Package setup
├── .env.example                   # Environment variables template
├── .gitignore
└── README.md
```

## ⚙️ Instalasi dan Setup

### Prerequisites
- Python 3.8+
- pip atau conda (direkomendasikan conda)

### 1. Clone Repository
```bash
git clone https://github.com/TurmaeUrsorum/bank-transaction-user-classification
cd bank-transaction-user-classification
```

### 2. Setup Environment

**Option A: menggunakan conda (sangat direkomendasikan)**
```bash
conda env create -f environment.yml
conda activate ds-project
```

**Option B: menggunakan pip**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows

# harus convert sendiri ke requirements.txt
pip install -r requirements.txt
```

## 🚀 Penggunaan

### Quick Start

1. Clone repository
2. Setup environment
3. Jalankan `kedro run`

```bash
# semua pipeline dijalankan
kedro run
# run kedro dengan parallel
kedro run --runner ParallelRunner
# run kedro spesifik pipeline
kedro run --pipeline data_EDA
```
## 🔬 Metodologi

### Data Preprocessing
- **Handling Missing Values**: [Technique yang digunakan]
- **Outlier Treatment**: [Method untuk handle outliers]
- **Encoding**: [Label encoding, One-hot encoding, etc.]
- **Scaling**: [Standardization/Normalization method]

### Feature Engineering
- **Created Features**: [feature yang dibuat amount to balance ratio dan multiple login flag ]

