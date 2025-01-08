# https://www.kaggle.com/datasets/vipullrathod/fish-market

import kagglehub

# Download latest version
path = kagglehub.dataset_download("vipullrathod/fish-market")


import pandas as pd
import os
from icecream import ic

path = os.path.join(path, "Fish.csv")

__all__ = ['path']

if __name__ == "__main__":
    ic(path)
    df = pd.read_csv(path)
    ic(df.head()) 