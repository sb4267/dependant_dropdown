import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import datetime
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
data = pd.read_csv('Data/new_autos_dropped.csv', sep=',',encoding='ISO-8859-1')
data = data.drop('Unnamed: 0',1)
data = data.drop('postal_code',1)
new_autos = data.copy()

le= LabelEncoder()
cat = new_autos.columns[new_autos.dtypes==object]
for col in cat:
    new_autos[col]= le.fit_transform(new_autos[col])
y=new_autos['price']
X=new_autos.drop(['price'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
#format
X_train.shape,y_train.shape,X_test.shape, y_test.shape

model=RandomForestRegressor(max_features = 4, max_depth= 20, min_samples_leaf= 1, oob_score=True,
                            min_samples_split= 3, n_estimators= 500,
                            n_jobs=-1)
model.fit(X_train,y_train)

def encode_input(df1):
    le= LabelEncoder()
    cat = df1.columns[df1.dtypes==object]
    for col in cat:
        df1[col]= le.fit_transform(df1[col])
    return df1

def Predict_Value(vt,gb,pp,m,km,ft,b,va):
    df1 = pd.DataFrame({ "vehicle_type":[vt],
                        "gearbox":[gb],
                        "power_ps":[pp],
                        "model":[m],
                        "kilometer":[km],
                        "fuel_type":[ft],
                        "brand":[b],
                        "vehicleAge":[va],})

    df2 = pd.DataFrame({ "vehicle_type":[0],
                        "gearbox":[0],
                        "power_ps":[0],
                        "model":[0],
                        "kilometer":[0],
                        "fuel_type":[0],
                        "brand":[0],
                        "vehicleAge":[0],})
    ndf1 = encode_input(df1)
    ndf1.append(df2, ignore_index = True)
    pred_price = model.predict(ndf1)
    return pred_price
