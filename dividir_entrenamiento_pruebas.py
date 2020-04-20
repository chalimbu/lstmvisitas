def dividir_entrenamiento_pruebas(porcentaje_pruebas,datos_x,datos_y):
    if type(porcentaje_pruebas) not in [float]:
        raise TypeError("se espera un float para el tamaño de los datos de pruebas")
    if (porcentaje_pruebas>1 or porcentaje_pruebas<0):
        raise ValueError("el porcentaje_pruebas debe estar entre 0 y 1")
    porcentaje_entrenamiento=1-porcentaje_pruebas
    limite_datos_entrenamiento=int(len(datos_y)*porcentaje_entrenamiento)
    return datos_x[:limite_datos_entrenamiento],datos_y[:limite_datos_entrenamiento],datos_x[limite_datos_entrenamiento:],datos_y[limite_datos_entrenamiento:]
