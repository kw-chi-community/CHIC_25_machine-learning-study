import pandas as pd
import matplotlib.pyplot as plt
from path import path
import os
from icecream import ic

df = pd.read_csv(path)

# boxplot들 확인해보니 knn으로 하기엔 weight랑 다른 feature들의 차이가 너무 큼 -> weight를 다른 값들의 크기로 맞춰주는 게 좋을듯

# 일반적으로 min-max scaling이 주로 사용됨 (https://oceanonx.tistory.com/21)
# new_value = (old_val - min_val) * (new_max - new_min) / (old_max - old_min) + new_min

old_min = df['Weight'].min()
old_max = df['Weight'].max()
new_min = 0
new_max = 60

df['scaled_weight'] = ((df['Weight'] - old_min) * (new_max - new_min) / (old_max - old_min) + new_min).round(1)

scaled_df = df.copy()

if __name__ == '__main__':
    ic(df[['Weight', 'scaled_weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']].head())