import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import sklearn
import shap

df = pd.read_csv("healthcare-dataset-stroke-data.csv")
df.to_csv("healthcare-dataset-stroke-data.csv", index = False)
df.head()

df = df.rename(columns={
                          "id":"ID",
                          "gender": "Sex",
                          "age": "Age",
                          "hypertension": "Hypertension",
                          "heart_disease": "Heart Disease",
                          "ever_married": "Ever Married?",
                          "work_type": "Work Type",
                          "Residence_type": "Residence Type",
                          "avg_glucose_level": "Avg Glucose Level",
                          "bmi": "BMI",
                          "smoking_status": "Smoking?",
                          "stroke": "Ever had a Stroke?"
                          })
df.head(10)

# Percentage of women
percentage_women = (df['Sex'] =='Female').mean() * 100

# Percentage of men
percentage_men = (df['Sex'] =='Male').mean() * 100

#Mean age 
mean_age = df["Age"].mean()

col1, col2 = st.columns(3)
col1.metric("Percentage of women (%)", f"{percentage_women: .2f}", border=True)
col2.metric("Percentage of men (%)", f"{percentage_men: .2f}", border=True)
col2.metric("Percentage of men (%)", f"{mean_age: .2f}", border=True)