import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import Normalizer
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

pdf = pd.read_csv("traffic_asia_later2021_unique_syd.csv", encoding = 'UTF-8', keep_default_na=False)
print(pdf.head())
print(pdf.corr(numeric_only = True))

x = pdf.iloc[:,[10,11]]
y1 = pdf.iloc[:, 13]

print(x)
print(y1)

X_train, X_test, y1_train, y1_test = train_test_split(x, y1, test_size=0.4, random_state=69)

model = LinearRegression()
model.fit(X_train,y1_train)

y1_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y1_test, y1_pred))
r2 = r2_score(y1_test, y1_pred)

residuals = y1_pred - y1_test 
plt.ioff()
plt.title("Testing")
plt.scatter(residuals, y1_pred)
plt.xlabel(pdf.columns[12] + ' ' + pdf.columns[10])
plt.ylabel(pdf.columns[13])
plt.show()
