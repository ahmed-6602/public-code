import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

 train = pd.read_csv("train (2).csv")

test = pd.read_csv("train (2).csv")

train.head(10)

train.tail(10)

test.head()

test.tail()

train.dtypes

train.shape

train.columns

train.isnull().sum()

train.describe()

train.info

train['Age'].value_counts()

plt.figure(figsize=(20,8))
sns.boxplot(data = train,width=0.8)
plt.show()

train.shape,test.shape

train['Age'].fillna(train['Age'].median(),inplace=True)

test['Age'].fillna(train['Age'].median(),inplace=True)

train['Age'].nunique



print(train['Embarked'].mode())
print(test['Embarked'].mode())

print(train['Embarked'].mode()[0])
print(test['Embarked'].mode()[0])

train['Embarked'].fillna(train['Embarked'].mode()[0],inplace = True)

test.isnull().sum()
train.isnull().sum()

train['Age'].min(),train['Age'].max()
plt.hist(train['Age'])
plt.show()

train['Embarked'].min(),train['Embarked'].max()
plt.hist(train['Embarked'])
plt.show()

train['Pclass'].min(),train['Pclass'].max()
plt.hist(train['Pclass'])
plt.show()

train['Fare'].min(),train['Fare'].max()
plt.hist(train['Fare'])
plt.show()

train.describe()

train['Fare'].quantile(0.88)

x_train = train.drop(['Fare'],axis=1)
y_train = train['Fare']

x_train.shape,y_train.shape

x_test = test.drop(['Fare'],axis=1)
y_test = test['Fare']

x_test.shape,y_test.shape



