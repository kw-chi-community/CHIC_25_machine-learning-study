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

length = df["Length1"]
weight = df["Weight"]

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = length
y = weight
z = length * length

ax.scatter(x, y, z)

ax.set_xlabel('length')
ax.set_ylabel('weight')
ax.set_zlabel('length^2')

script_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(script_dir, 'length_length_3d.png'))

from sklearn.linear_model import LinearRegression

X = np.column_stack((length, weight, length * length))

model1 = LinearRegression()
X1 = length.values.reshape(-1, 1)
model1.fit(X1, weight)
ic(model1.score(X1, weight))
ic(model1.coef_)
ic(model1.intercept_)

print("")

model2 = LinearRegression()
X2 = np.column_stack((length, length * length))
model2.fit(X2, weight)
ic(model2.score(X2, weight))
ic(model2.coef_)
ic(model2.intercept_)


print("-"*100)

# length
X_length = np.column_stack((weight, length * length))
model_length = LinearRegression()
model_length.fit(X_length, length)
ic(model_length.score(X_length, length))
ic(model_length.coef_)
ic(model_length.intercept_)

print("")

# weight
X_weight = np.column_stack((length, length * length))
model_weight = LinearRegression()
model_weight.fit(X_weight, weight)
ic(model_weight.score(X_weight, weight))
ic(model_weight.coef_)
ic(model_weight.intercept_)

print("")
# len^2
X_product = np.column_stack((length, weight))
model_product = LinearRegression()
model_product.fit(X_product, length * length)
ic(model_product.score(X_product, length * length))
ic(model_product.coef_)
ic(model_product.intercept_)


