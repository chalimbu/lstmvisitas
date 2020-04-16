from pandas import read_csv

def cargar_info(file_name):
    if type(file_name) not in [str]:
        raise TypeError("se espera un string para el nombre del archivo")
    ruta= "recursos/"+file_name
    read= read_csv(ruta, dtype = {"Usuarios": str },usecols=['Usuarios'])
    lista_individuales=list(map(lambda lista : lista[0],read.values))
    conversion_analitics=list(map(convertir_numero_formato_analitics,lista_individuales))
    return conversion_analitics

def convertir_numero_formato_analitics(numero):
    if type(numero) not in [str]:
        raise TypeError("se espera un string para la conversion")
    separados=numero.split(".")
    if (len(separados) == 1):
        return int(separados[0])
    elif (len(separados) == 2):
        multiplicador_segunda_parte=3-len(separados[1])
        nuevo_numero=(int(separados[0])*1000)+(int(separados[1])*(10**multiplicador_segunda_parte))
        return nuevo_numero
    else:
        raise ValueError("esta funcion solo soporte conversion hasta 999.999")
