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

df = pd.read_csv(path)
np_array = df.to_numpy()

ic(np_array[:10])

np_array_target = np.where(np_array[:, 0] == 'Bream', 1, 0)

ic(np_array_target[:10])

X = np_array[:, 1:].astype(float)
y = np_array_target

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)

X_scaled = (X - X_mean) / X_std
# 브로드캐스팅?
# X: 2차원
# X_mean: 1차원
# X_std: 1차원
# 1차원들 2차원으로 확장 후 계산 << 브로드캐스팅

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25)

ic(X_train.shape, X_test.shape) 
ic(y_train.shape, y_test.shape)

