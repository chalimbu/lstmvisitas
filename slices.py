
def obtener_slices_de_tamanio(lista_elementos,slice):
    if type(lista_elementos) not in [list]:
        raise TypeError("Se le debe pasar una lista para crear los slices de esta")
    if type(slice) not in [int]:
        raise TypeError("el tamaño de los slices debe ser un entero")
    if (slice <= 0):
        raise ValueError("El parametro slice debe ser mayor igual a 0 para poder crearlos")
    first_index=0
    last_index=slice
    list_with_slices=[]
    while (last_index<=len(lista_elementos)):
        list_with_slices.append(lista_elementos[first_index:last_index])
        first_index=first_index+1
        last_index=first_index+slice
    return list_with_slices
