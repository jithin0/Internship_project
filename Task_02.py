# Task 02:

## From the given ‘Iris’ dataset, predict the optimum number of clusters and represent it visually

## importing required packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns

print("Packages successfully imported")

### loading the dataset

from sklearn.datasets import load_iris

d = load_iris()
df = pd.DataFrame(d.data, columns = d.feature_names)
df.head()

df.tail()

df.info()

df.isnull().sum()

df.describe()

### plotting graph between different pairs (Ex: sepal length vs sepal width, etc...)

sns.pairplot(df)

plt.scatter(x = df["sepal length (cm)"], y =df["sepal width (cm)"])
plt.title("On Basis of Sapel")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()

plt.scatter(df["petal length (cm)"], df["petal width (cm)"])
plt.title("On Basis of Petal")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

### taking values for training

x = df.iloc[:,:].values

from sklearn.cluster import KMeans

### plotting Elbow graph

wcss = []

for i in range(1,11):
    km = KMeans(n_clusters = i)
    km.fit(x)
    wcss.append(km.inertia_)

plt.plot(range(1,11), wcss)
plt.xlabel("Num of clusters")
plt.show()

### from the elbow plot we can see that, the elbow structure is formed at the value 3. So the number of clusters is 3

km = KMeans(n_clusters = 3, init = "k-means++", max_iter = 300, n_init = 10, random_state=0)
y = km.fit_predict(x)
y

### ploting graph for visualizing the clusters

plt.figure(figsize = (12,7))
plt.scatter(x[y == 0,0], x[y == 0,1], label = 'setosa',color = 'red')
plt.scatter(x[y == 1,0], x[y == 1,1], label = 'versicolour', color='blue')
plt.scatter(x[y == 2,0], x[y == 2,1], label = 'verginica', color= 'green')

plt.title("On Basis of Sepal")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.legend()

plt.show()

plt.figure(figsize = (12,7))
plt.scatter(x[y == 0,2], x[y == 0,3], label = 'setosa',color = 'red')
plt.scatter(x[y == 1,2], x[y == 1,3], label = 'versicolour', color='blue')
plt.scatter(x[y == 2,2], x[y == 2,3], label = 'verginica', color= 'green')

plt.title("On Basis of Petal")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.legend()

plt.show()

