from sklearn.neighbors import KNeighborsClassifier
from _3_preprocessing import preprocessed_df
from sklearn.model_selection import train_test_split
from icecream import ic
df = preprocessed_df


X = df.drop('Species', axis=1)  
y = df['Species']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1)

knn.fit(X_train, y_train)

accuracy = knn.score(X_test, y_test)

if __name__ == '__main__':
    ic(accuracy) # 0.708...     왜 잘나옴..?