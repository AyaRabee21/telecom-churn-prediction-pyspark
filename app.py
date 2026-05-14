# app.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.linalg import Vectors

import os
import sys

# تحديد مسار Hadoop صراحةً
os.environ['HADOOP_HOME'] = "C:\\hadoop"
# إجبار النظام على إضافة مجلد bin إلى الـ PATH داخل بيئة بايثون الحالية
os.environ['PATH'] = os.environ['HADOOP_HOME'] + "\\bin;" + os.environ['PATH']

app = FastAPI()
templates = Jinja2Templates(directory="templates")


spark = SparkSession.builder \
    .master("local[*]") \
    .appName("ChurnAPI") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

model = RandomForestClassificationModel.load("model/churn_rf_model")

num_features = model.numFeatures
print(f"Loaded model with {num_features} features")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"my_variable": "القيمة هنا"})

@app.post("/predict")
async def predict(request: Request):
    form = await request.form()
    try:
        tenure = float(form.get("tenure", 0))
        monthly = float(form.get("MonthlyCharges", 0))
        total = float(form.get("TotalCharges", 0))
    except ValueError:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "prediction_text": "خطأ: من فضلك أدخل أرقامًا صحيحة."
        })

    
    # 1. هنعمل لستة فيها 19 صفر
    features = [0.0] * num_features
    
    # 2. هنحط كل رقم في مكانه التقريبي الصح
    # (الرقم بين القوسين [] هو الترتيب، تقدري تغيريه لو الترتيب في Colab مختلف)
    
    features[4] = tenure   # مدة الخدمة في الغالب بتكون الخانة الخامسة
    features[-2] = monthly # الرسوم الشهرية الخانة قبل الأخيرة
    features[-1] = total   # إجمالي الرسوم الخانة الأخيرة

    # prediction
    prediction = model.predict(Vectors.dense(features))
    result = "العميل سيرحل" if prediction == 1.0 else "العميل سيبقى"

    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"prediction_text": f"النتيجة: {result}"})