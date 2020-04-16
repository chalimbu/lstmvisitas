def extraer_data_modelo_persistente(datos):
    if type(datos) not in [list]:
        raise TypeError("se espera una lista de datos")
    for registro in datos:
        if type(registro) not in [list]:
            raise TypeError("se espera que cada registro sea un elemento con valor esperado y predicho")
        if len(registro) != 2 :
            raise ValueError("cada registro debe tener una longitud de 2 predicho y real")
    y_predicho=[] #equivaldra para el modelo persistente al registo anterior
    y_real = []
    for registro in datos:
        y_predicho.append(registro[0])
        y_real.append(registro[1])
    return y_predicho,y_real