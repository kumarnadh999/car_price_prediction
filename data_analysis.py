# -*- coding: utf-8 -*-
"""Data_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ShgLiDAN14UON8QPZnGRINxLZoBfzGdI
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('used_cars_data (1).csv')

print(df.head())

df['Mileage'] = df['Mileage'].str.extract('(\d+\.\d+)').astype(float)
df['Engine'] = df['Engine'].str.extract('(\d+)').astype(float)
df['Power'] = df['Power'].str.extract('(\d+\.\d+)').astype(float)

numeric_df = df.select_dtypes(include=['number'])
df[numeric_df.columns] = numeric_df.fillna(numeric_df.mean())

X = df[['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")