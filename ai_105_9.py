# -*- coding: utf-8 -*-
"""AI_105_9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/130yqZrinG14-hnyJcpJ6_w2UFGlpUNZ0
"""

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/zaferdemirkol/HerkesIcinYapayZeka/main/Advertising.csv")

X = df.drop('sales',axis=1)
y = df['sales']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train,y_train)

test_predictions = model.predict(X_test)

print(test_predictions)

model.score(X_test, y_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error

import numpy as np

MAE = mean_absolute_error(y_test,test_predictions)
MSE = mean_squared_error(y_test,test_predictions)
RMSE = np.sqrt(MSE)

MAE

MSE

RMSE

df['sales'].mean()

quartet = pd.read_csv('anscombes_quartet1.csv')

quartet

def model_olustur(x,y):
		model_quartet1 = LinearRegression()
		X_q1=x
		y_q1=y
		model_quartet1.fit(X_q1, y_q1)
		print(model_quartet1.coef_)
		print(model_quartet1.intercept_)
		MAE = mean_absolute_error(y_q1,model_quartet1.predict(X_q1))
		MSE = mean_squared_error(y_q1,model_quartet1.predict(X_q1))
		print(MAE)
		print(MSE)

model_olustur(quartet[["x"]], quartet["y"])

quartet['pred_y'] = 3 + 0.5 * quartet['x']
quartet['residual'] = quartet['y'] - quartet['pred_y']

import seaborn as sns
sns.scatterplot(data=quartet,x='x',y='y')
sns.lineplot(data=quartet,x='x',y='pred_y',color='red')

sns.kdeplot(quartet['residual'])

import matplotlib.pyplot as plt

sns.scatterplot(data=quartet,x='y',y='residual')
plt.axhline(y=0, color='r', linestyle='--')

quartet = pd.read_csv('anscombes_quartet2.csv')

model_olustur(quartet[["x"]], quartet["y"])

quartet['pred_y'] = 3 + 0.5 * quartet['x']
quartet['residual'] = quartet['y'] - quartet['pred_y']

sns.scatterplot(data=quartet,x='x',y='y')
sns.lineplot(data=quartet,x='x',y='pred_y',color='red')

sns.kdeplot(quartet['residual'])

sns.scatterplot(data=quartet,x='y',y='residual')
plt.axhline(y=0, color='r', linestyle='--')

quartet = pd.read_csv('anscombes_quartet4.csv')

model_olustur(quartet[["x"]], quartet["y"])

quartet['pred_y'] = 3 + 0.5 * quartet['x']
quartet['residual'] = quartet['y'] - quartet['pred_y']

sns.scatterplot(data=quartet,x='x',y='y')
sns.lineplot(data=quartet,x='x',y='pred_y',color='red')

sns.kdeplot(quartet['residual'])

sns.scatterplot(data=quartet,x='y',y='residual')
plt.axhline(y=0, color='r', linestyle='--')

test_predictions = model.predict(X_test)

test_res = y_test - test_predictions

sns.scatterplot(x=y_test,y=test_res)
plt.axhline(y=0, color='r', linestyle='--')

sns.kdeplot(test_res)

final_model = LinearRegression()

final_model.fit(X,y)

y_hat = final_model.predict(X)

fig,axes = plt.subplots(nrows=1,ncols=3,figsize=(16,6))

axes[0].plot(df['TV'],df['sales'],'o')
axes[0].plot(df['TV'],y_hat,'o',color='red')
axes[0].set_ylabel("Sales")
axes[0].set_title("TV Spend")


axes[1].plot(df['radio'],df['sales'],'o')
axes[1].plot(df['radio'],y_hat,'o',color='red')
axes[1].set_ylabel("Sales")
axes[1].set_title("Radio Spend")


axes[2].plot(df['newspaper'],df['sales'],'o')
axes[2].plot(df['newspaper'],y_hat,'o',color='red')
axes[2].set_ylabel("Sales")
axes[2].set_title("newspaper Spend")

residuals = y_hat - y

sns.scatterplot(x=y,y=residuals)
plt.axhline(y=0, color='r', linestyle='--')

final_model.coef_

coeff_df = pd.DataFrame(final_model.coef_,X.columns,columns=['Coefficient'])
coeff_df

df.corr().T

campaign = [[149,22,12]]

final_model.predict(campaign)

from joblib import dump, load

dump(final_model, "sales_model.joblib")

loaded_model = load("sales_model.joblib")

loaded_model.predict(campaign)

"""# Polynom Regresyon"""

veriler=pd.read_csv("masraflar.csv")
veriler

x=veriler["gün"]
y=veriler["harcama"]

plt.scatter(x, y, label='Gerçek Veriler')

coefficients = np.polyfit(x, y, 2)

polynomial = np.poly1d(coefficients)

y_pred = polynomial(x)

plt.scatter(x, y, label='Gerçek Veriler')
plt.plot(x, y_pred, color='r', label='2. Dereceden Polinom')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

gun=veriler.iloc[:,0:1]

Harcama=veriler.iloc[:,1:2]

from sklearn.linear_model import LinearRegression
linReg = LinearRegression()
LModel=linReg.fit(gun, Harcama)

plt.scatter(gun, Harcama)
plt.plot(gun, LModel.predict(gun), color="red")

from sklearn.metrics import mean_squared_error, mean_absolute_error

LModel.score(gun, Harcama)

MAE = mean_absolute_error(y, LModel.predict(gun))
print(MAE)
MSE = mean_squared_error(y,LModel.predict(gun))
print(MSE)
RMSE = np.sqrt(MSE)
print(RMSE)

from sklearn.preprocessing import PolynomialFeatures
polReg=PolynomialFeatures(degree=2,include_bias=False)

gun

gun_pol=polReg.fit_transform(gun)

gun_pol

linReg2 = LinearRegression()

linReg2.fit(gun_pol, Harcama)

plt.scatter(gun, Harcama)
plt.plot(gun, linReg2.predict(gun_pol), color="red")

linReg2.score(gun_pol, Harcama)

MAE = mean_absolute_error(y, linReg2.predict(gun_pol))
print(MAE)
MSE = mean_squared_error(y,linReg2.predict(gun_pol))
print(MSE)
RMSE = np.sqrt(MSE)
print(RMSE)

10.355467888640376
158.40064446527427
12.585731781079488

"""# Çok özellikli polynom reg"""

df = pd.read_csv("https://raw.githubusercontent.com/zaferdemirkol/HerkesIcinYapayZeka/main/Advertising.csv")
df

X = df.drop('sales',axis=1)
y = df['sales']

X.shape

from sklearn.preprocessing import PolynomialFeatures

polynomial_converter = PolynomialFeatures(degree=2,include_bias=False)

poly_features = polynomial_converter.fit_transform(X)

poly_features.shape

"""[x1, x2, x3]

Bu dizinin 2. dereceden çıktısı
[x1, x2, x3, x1^2, x1*x2, x1*x3, x2^2, x2*x3, x3^2]



"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=101)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train,y_train)

test_predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error,mean_squared_error

model.score(X_test, y_test)

"""score:0.91

MAE: 1.21

MSE: 2.30

RMSE: 1.51


0.4896798044803838

0.4417505510403753

0.6646431757269274



"""

MAE = mean_absolute_error(y_test,test_predictions)
MSE = mean_squared_error(y_test,test_predictions)
RMSE = np.sqrt(MSE)

print(MAE)
print(MSE)
print(RMSE)

train_rmse_errors = []
test_rmse_errors = []


for d in range(1,10):

    polynomial_converter = PolynomialFeatures(degree=d)
    poly_features = polynomial_converter.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=101)

    model = LinearRegression()
    model.fit(X_train,y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_RMSE = np.sqrt(mean_squared_error(y_train,train_pred))
    test_RMSE = np.sqrt(mean_squared_error(y_test,test_pred))

    train_rmse_errors.append(train_RMSE)
    test_rmse_errors.append(test_RMSE)

train_rmse_errors

test_rmse_errors

plt.plot(range(1,6),train_rmse_errors[:5],label='TRAIN')
plt.plot(range(1,6),test_rmse_errors[:5],label='TEST')
plt.xlabel("Polynomial Complexity")
plt.ylabel("RMSE")
plt.legend()

final_poly_converter = PolynomialFeatures(degree=3,include_bias=False)

final_model = LinearRegression()

final_model.fit(final_poly_converter.fit_transform(X),y)

from joblib import dump, load

dump(final_model, 'sales_poly_model.joblib')

dump(final_poly_converter,'poly_converter.joblib')

loaded_poly = load('poly_converter.joblib')
loaded_model = load('sales_poly_model.joblib')

campaign = [[149,22,12]]

campaign_poly = loaded_poly.transform(campaign)

loaded_model.predict(campaign_poly)

"""# L1, L2 Düzeltimler (Cezalandırmalar)"""

plt.figure(figsize=(10,7))

x = np.array([105,118,120,126,133,135, 135])
y = np.array([208,220,215,228,228,223,235])
m, b = np.polyfit(x, y, 1)

plt.plot(x,y, "ro")
plt.plot(x, m*x+b,"r")



plt.figure(figsize=(10,7))

x = np.array([105,118,120,126,133,135, 135])
y = np.array([208,220,215,228,228,223,235])
m, b = np.polyfit(x, y, 1)



plt.plot(x,y, "ro")
plt.plot(x, m*x+b,"r")



x2 = np.array([113,123,140,142,144])
y2 = np.array([212,218,228, 224,228])
plt.plot(x2,y2, "bo")



xt = np.array([105,118,120,126,133,135, 135, 113,123,140,142,144])
yt = np.array([208,220,215,228,228,223,235,212,218,228, 224,228])
m2, b2 = np.polyfit(xt,yt, 1)
plt.plot(xt, m2*xt+b2,"b")

X = x.reshape(-1, 1)
y = y.reshape(-1, 1)
X_test=x2.reshape(-1, 1)
y2=y2.reshape(-1,1)
xt=xt.reshape(-1,1)
yt=yt.reshape(-1,1)

reg = LinearRegression()
model = reg.fit(X, y)

print("intercept: ", model.intercept_)
print("coef: ", model.coef_)

predict = model.predict(X)

plt.plot(X,y, "ro")
plt.plot(X, predict,"r")

from sklearn.metrics import mean_absolute_error

train_predictions = model.predict(X)
MAE = mean_absolute_error(y,train_predictions)
MAE

test_predictions = model.predict(X_test)
MAE = mean_absolute_error(y2,test_predictions)
MAE

total_predictions = model.predict(xt)
MAE = mean_absolute_error(yt,total_predictions)
MAE

from sklearn.linear_model import Ridge

rmodel=Ridge(alpha=1000).fit(X, y)

print("intercept: ", rmodel.intercept_)
print("coef: ", rmodel.coef_)

intercept:  [133.89697909]
coef:  [[0.71068939]]

rpredict = rmodel.predict(X)
plt.plot(X,y, "ro")
plt.plot(X, rpredict,"r")
plt.plot(X, predict,"g")
plt.plot(x2, y2,"bo")

rtrain_predictions = rmodel.predict(X)
MAE = mean_absolute_error(y,rtrain_predictions)
MAE

rtest_predictions = rmodel.predict(X_test)
MAE = mean_absolute_error(y2,rtest_predictions)
MAE

rtotal_predictions = rmodel.predict(xt)
MAE = mean_absolute_error(yt,rtotal_predictions)
MAE

"""
## Linear Train MAE: 3.4165099037291133

## Lineer Test MAE: 5.992254066615021

## Lineer Total MAE: 4.489736638264908


## Ridge  Train MAE: 5.026823883121149
## Ridge  Test MAE: 3.1571193686287415
## Ridge Total MAE: 4.247780335415979"""

