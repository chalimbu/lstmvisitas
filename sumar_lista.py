def sumar_lista(lista):
    if type(lista) not in [list]:
        raise TypeError("para sumar los elementos de la lista se espera una lista")
    for elemento in lista:
        if type(elemento) not in [int, float]:
            raise TypeError("todos los elementos de la lista deben ser int o float para sumarlos")

    acumulador=0
    for bandera in lista:
        acumulador=acumulador+bandera
    return acumulador