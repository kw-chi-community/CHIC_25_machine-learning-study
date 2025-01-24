import pandas as pd
import os
from icecream import ic
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
path = os.path.join(parent_dir, '1주차', 'fish_market')
sys.path.append(path)
import matplotlib.pyplot as plt

from path import path

import numpy as np

df = pd.read_csv(path)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

train_feature, test_feature, train_target, test_target = train_test_split(df["Length1"], df["Weight"], test_size=0.2) # Length에 따른 Weight만

plt.scatter(train_feature, train_target)
plt.scatter(test_feature, test_target)
script_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(script_dir, 'length1_weight.png'))

poly = PolynomialFeatures(degree=2)

# poly.fit([[2,3,4,5],[2,3,4,5]])
# train_poly = poly.transform([[2,3,4,5],[2,3,4,5]])
# ic(train_poly)

poly.fit(train_feature)
train_poly = poly.transform(train_feature) # ValueError: Expected a 2-dimensional container but got <class 'pandas.core.series.Series'> instead. Pass a DataFrame containing a single row (i.e. single sample) or a single column (i.e. single feature) instead. 여기서 trainform이 어케 작동하기에 2-dimentional container가 필요하다 하는 거지
test_poly = poly.transform(test_feature)

ic(train_poly.shape)
ic(test_poly.shape)
