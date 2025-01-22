import pandas as pd
import os
from icecream import ic
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
path = os.path.join(parent_dir, '1주차', 'fish_market')
sys.path.append(path)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor
from path import path

df = pd.read_csv(path)

length = df["Length1"] # feature
length_sq = length * length # feature
weight = df["Weight"] # target


model = LinearRegression()
X = np.column_stack((length, length_sq))
model.fit(X, weight)

ic(model.score(X, weight)) # 0.8471568046967375
ic(model.coef_) # array([19.19473177,  0.23321982])
ic(model.intercept_) # np.float64(-289.3081630608135)

X_df = pd.DataFrame({'length': length, 'length_sq': length_sq})

correlation = X_df.corr()
ic(correlation)

"""
ic| correlation:              length  length_sq
                 length     1.000000   0.971355
                 length_sq  0.971355   1.000000
"""

