from sklearn.metrics import mean_squared_error
from math import sqrt

def calcular_raiz_error_cuadratico_medio(y_true,y_pred):
    if type(y_true) not in [list]:
        raise TypeError("se espera que y_true sea una lista")
    if type(y_pred) not in [list]:
        raise TypeError("se espera que y_pred sea una lista")
    for y_true_registro in y_true:
        if type(y_true_registro) not in [int,float]:
            raise TypeError("se espera que los valores sean numeros o flotantes")
    for y_pred_registro in y_pred:
        if type(y_pred_registro) not in [int, float]:
            raise TypeError("se espera que los valores sean numeros o flotantes")
    if len(y_true) != len(y_pred):
        raise ValueError("los valores predichos y reales deben mantener la misma cantida de registros")
    rmse= sqrt(mean_squared_error(y_true, y_pred))
    return rmse