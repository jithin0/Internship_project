# Task : 01

'''Prediction using Supervised ML.
Predict the percentage of an student based on the no. of study hours'''

### Importing required packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

print("Packages successfully installed")

### importing dataset

df = pd.read_csv("https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv")
df.head()

df.shape

df.info()

df.describe()

## ploting graph (hours vs scores)

df.plot(x="Hours",y="Scores",style="o")
plt.title("Hours vs Scores")
plt.xlabel("Hours studied")
plt.ylabel("Scores secured")
plt.show()

### Importing Machile learning modules for training and prediction

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("successfully installed")

# seperating values for training
x = df.iloc[:,:1].values
y = df.iloc[:,1].values
#print(y)
#print(x)

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state = 0)

reg = LinearRegression()

# fitting the traing data

reg.fit(x_train,y_train)

line = reg.coef_*x + reg.intercept_
plt.scatter(x, y, color = "orange")
plt.plot(x, line, color = "red")
plt.show()

## Predicting values for x_test

y_pred = reg.predict(x_test)
y_pred

pd.DataFrame({"Actual values":y_test, "Predicted values" : y_pred})

## Score obtained for 9.25 hours of studying

reg.predict([[9.25]])

## calculating error

from sklearn.metrics import mean_absolute_error

mean_absolute_error(y_test, y_pred)

