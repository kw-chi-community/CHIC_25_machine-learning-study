import kagglehub

# Download latest version
path = kagglehub.dataset_download("vipullrathod/fish-market")

import pandas as pd
import os
from icecream import ic
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
import time
import resource

ic(path)
df = pd.read_csv(os.path.join(path, "Fish.csv"))
ic(df.head()) 

columns_to_multiply = ['Weight', 'Length1', 'Length2', 'Length3']

scaler = MinMaxScaler()
df[columns_to_multiply] = scaler.fit_transform(df[columns_to_multiply])

df = df.drop(['Height', 'Width'], axis=1)

ic(df.head()) 


X = df.drop('Species', axis=1)  
y = df['Species']  

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

class knns:
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X.values 
        self.y_train = y.values 
        
    def predict(self, X):
        predictions = []
        for x in X.values:
            distances = []
            for train_x in self.X_train:
                distance = 0
                for i in range(len(x)):
                    distance += (train_x[i] - x[i]) ** 2
                distances.append(distance)
            
            k_indices = []
            distances_enum = list(enumerate(distances))
            distances_enum.sort(key=lambda x: x[1])
            k_indices = [idx for idx, _ in distances_enum[:self.k]]
            
            k_nearest_labels = [self.y_train[i] for i in k_indices]
            label_counts = {}
            for label in k_nearest_labels:
                label_counts[label] = label_counts.get(label, 0) + 1
            
            most_common = max(label_counts.items(), key=lambda x: x[1])[0]
            predictions.append(most_common)
            
        return predictions

if __name__ == "__main__":
    total_time = 0
    total_cpu_time = 0
    iter = 1000
    
    for i in range(iter):
        start_time = time.time()
        start_cpu_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime
        
        knn = knns(k=10)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        
        end_time = time.time()
        end_cpu_time = resource.getrusage(resource.RUSAGE_SELF).ru_utime
        
        total_time += (end_time - start_time)
        total_cpu_time += (end_cpu_time - start_cpu_time)
        
        if i % 100 == 0:
            ic(i)
    
    average_time = total_time / iter
    average_cpu_time = total_cpu_time / iter
    accuracy = accuracy_score(y_test, y_pred)
    
    ic(accuracy)
    ic(average_time)
    ic(average_cpu_time)
    ic(total_time)
    ic(total_cpu_time)