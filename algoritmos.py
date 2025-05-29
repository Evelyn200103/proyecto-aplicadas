import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

def arbol_decision(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col]
    modelo = DecisionTreeClassifier()
    modelo.fit(X, y)
    predicciones = modelo.predict(X)
    return predicciones

def k_means(df, n_clusters=3):
    modelo = KMeans(n_clusters=n_clusters)
    modelo.fit(df)
    return modelo.labels_

def regresion_lineal(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col]
    modelo = LinearRegression()
    modelo.fit(X, y)
    predicciones = modelo.predict(X)
    return predicciones

