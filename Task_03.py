# Task 03:

## Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’

### ● As a business manager, try to find out the weak areas where you can work to make more profit.
### ● What all business problems you can derive by exploring the data? 


### importing required packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

print("successfully installed")

## loading dataset

df = pd.read_csv("SampleSuperstore.csv")
df.head()

df.drop("Postal Code", axis = 1, inplace = True)
df.head()

df.info()

df.describe()

## Plotinng Discount vs Profit graph

plt.figure(figsize = (12,8))
plt.scatter(df["Discount"], df["Profit"])
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

### as we can see Profit decreases with increase in Discount



## Ploting Sales vs Profit 

plt.figure(figsize = (12,8))
plt.scatter(df["Sales"], df["Profit"])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

### as we guessed Profit gets high withrespect to Sales

kv_pair = dict()
for i in range(9994):
    if df['Sub-Category'][i] in kv_pair:
        kv_pair[df['Sub-Category'][i]] += df['Sales'][i]
    else:
        kv_pair[df['Sub-Category'][i]] = df['Sales'][i]
        
print(kv_pair)

x1 = kv_pair.keys()
y1 = kv_pair.values()

## Ploting Sub-Category vs Sales (to find which products had been sold more)

fig1, ax1 = plt.subplots()
ax1.pie(y1, labels=x1, radius=5000)
ax1.axis('equal')
plt.show()

### as we can see Phones, Chairs and some other are sold more 

kv_pair2 = dict()
for i in range(9994):
    if df['Sub-Category'][i] in kv_pair2:
        kv_pair2[df['Sub-Category'][i]] += df['Profit'][i]
    else:
        kv_pair2[df['Sub-Category'][i]] = df['Profit'][i]
        
print(kv_pair2)

## Products vs Profit (to find which product makes more Profit)

x2 = kv_pair2.keys()
y2 = kv_pair2.values()

plt.plot(y, x, 'bo')

### as the result, Machines are making more profit than any other products

kv_pair3 = dict()
for i in range(9994):
    if df['Region'][i] in kv_pair3:
        kv_pair3[df['Region'][i]] += df['Sales'][i]
    else:
        kv_pair3[df['Region'][i]] = df['Sales'][i]
        
print(kv_pair3)

## Region vs Sales (to find where the most products are sold)

fig2, ax2 = plt.subplots()
ax2.pie(kv_pair3.values(), labels = kv_pair3.keys())
ax2.axis('equal')
plt.show()

### as we can see More Products are sold in West and East region 

kv_pair4 = dict()
for i in range(9994):
    if df['Region'][i] in kv_pair4:
        kv_pair4[df['Region'][i]] += df['Profit'][i]
    else:
        kv_pair4[df['Region'][i]] = df['Profit'][i]
        
print(kv_pair4)

## Region vs Profit (to find where the Profit is more)

fig3, ax3 = plt.subplots()
ax3.pie(kv_pair4.values(), labels = kv_pair4.keys())
ax3.axis('equal')
plt.show()

### as the graph shows, we are making more profits in west and east regions

kv_pair5 = dict()
for i in range(9994):
    if df['State'][i] in kv_pair5:
        kv_pair5[df['State'][i]] += df['Sales'][i]
    else:
        kv_pair5[df['State'][i]] = df['Sales'][i]
        
print(kv_pair5)

## States vs Sales (to find where we are selling more products)

plt.figure(figsize=(8,12))
plt.plot(kv_pair5.values(), kv_pair5.keys(), 'bo')
plt.show()

### we can see that we are selling more Products in California, New york , etc.. 
### and a very few in Nebraska, lowa, etc...

kv_pair6 = dict()
for i in range(9994):
    if df['State'][i] in kv_pair6:
        kv_pair6[df['State'][i]] += df['Profit'][i]
    else:
        kv_pair6[df['State'][i]] = df['Profit'][i]
        
print(kv_pair6)

## States vs Profits

plt.figure(figsize=(8,12))
plt.plot(kv_pair6.values(), kv_pair6.keys(), 'bo')
plt.show()

### as expected California and Newyork has high Profit rate
### and we can see that, eventhough Texas has high sales rate it has only very poor profit rate

kv_pair7 = dict()
for i in range(9994):
    if df['Segment'][i] in kv_pair7:
        kv_pair7[df['Segment'][i]] += df['Sales'][i]
    else:
        kv_pair7[df['Segment'][i]] = df['Sales'][i]
        
print(kv_pair7)

## People category vs Sales (to find who bought more products)

fig4, ax4 = plt.subplots()
ax4.pie(kv_pair7.values(), labels = kv_pair7.keys())
ax4.axis('equal')
plt.show()

### as we can see that Consumers are buying more that Corporates and home office

kv_pair8 = dict()
for i in range(9994):
    if df['Segment'][i] in kv_pair8:
        kv_pair8[df['Segment'][i]] += df['Profit'][i]
    else:
        kv_pair8[df['Segment'][i]] = df['Profit'][i]
        
print(kv_pair8)

## People category vs Profits 

fig5, ax5 = plt.subplots()
ax5.pie(kv_pair8.values(), labels = kv_pair8.keys())
ax5.axis('equal')
plt.show()

### Eventhough corporate has less sales rate, it almost have equal Profit rate as Consumer

df['Country'].unique() ### to check if it has any other that USA

# Result :
## we can INCREASE THE PROFIT,
###    - if we increase the sales of Machines and Phones. Ecspeacially eventhough Machines has low sales rate it has very high Profit rate
###    - if we decrease the Discount rate
###    - we should introduce more products in West and East region as it has high sales and profit rates
###    - we can increase the sales in California as it has very high Profit rate
###    - we can concentrate to increase the sales in Corporate as it has High profit rate

