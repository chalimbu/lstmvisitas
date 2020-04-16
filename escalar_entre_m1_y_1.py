def escalar_entre_m1_y_1(lista):
    if type(lista) not in [list]:
        raise TypeError("para escalar los elementos de la lista se espera una lista")
    for elemento in lista:
        if type(elemento) not in [int, float]:
            raise TypeError("se espera una lista de int,float para escalar")
    if len(lista) <= 1:
        raise ValueError("la lista debe tener 2 elementos para escalarse")
    if len(set(lista)) <= 1:
        raise ValueError("la lista debe tener almenos 2 elemento de DISTINTO valor para escalarse")
    rmin=lista[0]
    rmax=lista[0]
    for i in lista:
        if(i < rmin):
            rmin=i
        if(i > rmax):
            rmax=i
    tmax=1
    tmin=-1
    nueva_lista=[]
    for m in lista:
        nuevo_elemento = ((( m - rmin )/( rmax - rmin ))*( tmax - tmin )) + tmin
        nueva_lista.append(nuevo_elemento)
    return rmin,rmax,nueva_lista

