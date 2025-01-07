# 이걸 먼저 scailing보다 먼저 했었어야

# weight의 min 값이 0 << 얘를 결측치로 처리했어야 했던 거 아닌가

import pandas as pd
import numpy as np
from _2_scailing import scaled_df
from icecream import ic

df = scaled_df

df = df.drop(columns=['Weight'])

zero_weight_count = df[df['scaled_weight'] == 0].shape[0] # 1개밖에 없으니 그냥 버립시다..
df = df[df['scaled_weight'] != 0]

preprocessed_df = df.copy()

if __name__ == '__main__':
    ic(zero_weight_count)
    ic(preprocessed_df.head())