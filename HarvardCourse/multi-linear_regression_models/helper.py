import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('../data_sets/Advertising.csv')
df = df.drop(columns=['Unnamed: 0'])

def fit_and_plot_linear(predictor):
    """
    Ajusta un modelo lineal para un predictor dado y calcula los valores de R-cuadrado
    para los conjuntos de entrenamiento y prueba.
    """
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(predictor, df['Sales'], test_size=0.2, random_state=42)

    # Ajustar el modelo lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predecir y calcular R-cuadrado
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    r2_train = r2_score(y_train, y_train_pred)
    r2_test = r2_score(y_test, y_test_pred)

    # Graficar los resultados
    plt.scatter(X_train, y_train, color='blue', label='Train Data')
    plt.scatter(X_test, y_test, color='green', label='Test Data')
    plt.plot(X_train, y_train_pred, color='red', label='Model')
    plt.legend()
    plt.title('Linear Regression')
    plt.show()

    return r2_train, r2_test

def fit_and_plot_multi():
    """
    Ajusta un modelo multivariado y calcula los valores de R-cuadrado
    para los conjuntos de entrenamiento y prueba.
    """
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Ajustar el modelo multivariado
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predecir y calcular R-cuadrado
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    r2_train = r2_score(y_train, y_train_pred)
    r2_test = r2_score(y_test, y_test_pred)

    # Graficar los resultados
    plt.scatter(y_train, y_train_pred, color='blue', label='Train Data')
    plt.scatter(y_test, y_test_pred, color='green', label='Test Data')
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', label='Perfect Fit')
    plt.legend()
    plt.title('Multi-linear Regression')
    plt.show()

    return r2_train, r2_test