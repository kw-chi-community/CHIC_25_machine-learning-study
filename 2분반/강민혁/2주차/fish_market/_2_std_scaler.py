import pandas as pd
import os
from icecream import ic
import sys
current_dir = os.path.dirname(os.path.abspath(__file__)) # 조금 더 깔끔하게 안되나.. docker 묶었을 때 이러면 무조건 뭔가뭔가 생길 거 같은데
parent_dir = os.path.dirname(os.path.dirname(current_dir))
path = os.path.join(parent_dir, '1주차', 'fish_market')
sys.path.append(path)

from path import path

ic(path)

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


df = pd.read_csv(path)
np_array = df.to_numpy()

ic(np_array[:10])

np_array_target = np.where(np_array[:, 0] == 'Bream', 1, 0)

ic(np_array_target[:10])

X = np_array[:, 1:].astype(float)
y = np_array_target

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)

X_scaled_manual = (X - X_mean) / X_std

scaler = StandardScaler()
X_scaled_sklearn = scaler.fit_transform(X)


script_dir = os.path.dirname(os.path.abspath(__file__))


n_features = X.shape[1]
fig, axes = plt.subplots(n_features, 1, figsize=(12, 4*n_features))
feature_names = ['Length', 'Height', 'Width', 'Weight', 'Length2', 'Height2', 'Width2']

for i in range(n_features):
    difference = X_scaled_manual[:, i] - X_scaled_sklearn[:, i]
    axes[i].bar(range(len(difference)), difference, alpha=0.5)
    axes[i].set_title(feature_names[i])
    axes[i].grid(True)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, '1_compare_scaler_vs_manual.png'))
