# 📡 Telco Customer Churn Prediction (Big Data Approach)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![PySpark](https://img.shields.io/badge/PySpark-Big_Data-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Web_Framework-green.svg)

## 📖 Project Overview (نبذة عن المشروع)
This project aims to predict whether a telecom customer will churn (leave the service) or stay, based on their account and demographic data. 

**Big Data Technology:** Unlike traditional machine learning models that use Pandas and Scikit-Learn, this project is built from the ground up using **Apache Spark (PySpark)**. This allows the system to scale efficiently and handle massive amounts of Big Data across distributed clusters. The machine learning model (Random Forest) was trained using Spark MLlib, and the predictions are served via a fast and modern API built with **FastAPI**.

---

## 📊 Dataset (مجموعة البيانات)
The model was trained on the famous IBM Telco Customer Churn dataset available on Kaggle.
* **Link:** [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/code)

---

## 🛠️ Technologies Used (التقنيات المستخدمة)
* **Big Data Engine:** Apache Spark (PySpark), Hadoop (Winutils)
* **Machine Learning:** Spark MLlib (Random Forest Classifier)
* **Backend Framework:** FastAPI, Uvicorn
* **Frontend:** HTML5, CSS, Jinja2 Templates

---

## ⚙️ Installation & Setup (كيفية التثبيت والتشغيل)

Follow these steps to run the project on your local machine:

### 1. Clone the repository (نسخ المشروع)
```bash
git clone [https://github.com/AyaRabee21/telecom-churn-prediction-pyspark.git](https://github.com/AyaRabee21/telecom-churn-prediction-pyspark.git)
cd telecom-churn-prediction-pyspark

```

### 2. Create a Virtual Environment (إنشاء بيئة وهمية)

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For Mac/Linux

```

### 3. Install Requirements (تثبيت المكتبات المطلوبة)

```bash
pip install -r requirements.txt

```

### 4. Hadoop / PySpark Setup for Windows (إعدادات ويندوز)

If you are running this on Windows, you need Hadoop native libraries (`winutils.exe` and `hadoop.dll`).

1. Download them and place them in a folder (e.g., `C:\hadoop\bin`).
2. The `app.py` script automatically configures `HADOOP_HOME` to point to this directory.

### 5. Run the Application (تشغيل السيرفر)

```bash
uvicorn app:app --reload

```

### 6. Usage (الاستخدام)

Open your web browser and go to:

* **http://localhost:8000**
Enter the customer details (Tenure, Monthly Charges, Total Charges) and click Predict.

---
### Result :

https://github.com/user-attachments/assets/f79dbef7-dee0-400d-b295-85ac92ddcfa2






https://github.com/user-attachments/assets/58e4d7fe-7ea3-4906-a219-72ea3476334b


