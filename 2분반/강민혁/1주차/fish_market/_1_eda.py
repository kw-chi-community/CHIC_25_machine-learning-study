import pandas as pd
import matplotlib.pyplot as plt
from path import path
import os
from icecream import ic

df = pd.read_csv(path)

# 단위는..?
ic(df.head())
ic(df.dtypes)
ic(df.isnull().sum())
ic(df.describe())

y_variables = [col for col in df.columns if col not in ['Weight', 'Species']]

plt.figure(figsize=(15, 10))
for i, column in enumerate(y_variables, 1):
    plt.subplot(2, 3, i)
    for species in df['Species'].unique():
        species_data = df[df['Species'] == species]
        plt.scatter(species_data['Weight'], species_data[column], 
                    label=species, s=3)
    plt.xlabel('weight')
    plt.ylabel(column)
    plt.title(column)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
script_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(script_dir, '1_eda_1_scatter.png'), bbox_inches='tight')

variables = [col for col in df.columns if col != 'Species']

plt.figure(figsize=(15, 10))
for i, species in enumerate(df['Species'].unique(), 1):
    plt.subplot(2, 4, i)
    species_data = df[df['Species'] == species]
    
    plot_data = species_data[variables]
    
    plt.boxplot(plot_data, tick_labels=variables) # MatplotlibDeprecationWarning: The 'labels' parameter of boxplot() has been renamed 'tick_labels' since Matplotlib 3.9; support for  the old name will be dropped in 3.11. 대체 왜...?
    #
    # `tick_labels`는 x축이나 y축 레이블
    # `label`은 legend 표시할 때 사용

    plt.xticks(rotation=45)
    plt.title(species)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, '1_eda_2_boxplot.png'), bbox_inches='tight')

plt.figure(figsize=(15, 10))
for i, feature in enumerate(variables, 1):
    plt.subplot(2, 3, i)
    
    plt.boxplot([df[df['Species'] == species][feature] for species in df['Species'].unique()],
                tick_labels=df['Species'].unique())
    
    plt.xticks(rotation=45)
    plt.title(feature)
    plt.ylabel(feature)

plt.tight_layout()
plt.savefig(os.path.join(script_dir, '1_eda_3_boxplot22.png'), bbox_inches='tight')