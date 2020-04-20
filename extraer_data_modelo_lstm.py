import numpy

def extraer_data_modelo_lstm(datos):
    if type(datos) not in [list]:
        raise TypeError("se espera una lista de datos")
    if(len(datos)==0):
        raise ValueError("se debe tener almenos un registro para extraer el modelo")
    if type(datos[0]) not in [list]:
        raise TypeError("se espera que cada registro sea una lista de de datos")
    tamanio_de_datos=len(datos[0])
    for registro in datos:
        if type(registro) not in [list]:
            raise TypeError("se espera que cada registro sea una lista de datos")
        if (len(registro) != tamanio_de_datos):
            raise ValueError("todas las listas de registro deben ser del mismo tamaño")
    valores_x=[]
    valores_y=[]
    for registro in datos:
        #los valores x(entrada) son todos menos el ultimo
        lista_previa=list(map(lambda registro: [registro],registro[:-1]))
        valores_x.append(lista_previa)
        valores_y.append(registro[len(registro)-1])
    return numpy.array(valores_x,dtype=numpy.float32) ,numpy.array(valores_y,dtype=numpy.float32)