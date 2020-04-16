def generar_lista_con_saltos(tamanio_listas,salto_entre_elemento,lista):
    if type(lista) not in [list]:
        raise TypeError("se espera una lista en el parametro lista para generar una lista con saltos")
    if type(tamanio_listas) not in [int]:
        raise TypeError("se espera un entero")
    if type(salto_entre_elemento) not in [int]:
        raise TypeError("se espera un entero")
    if (salto_entre_elemento <= 0) :
        raise ValueError("el salto debe ser almenos 1(es decir sin saltar elementos")
    lista_final=[]
    indice_inicio=0
    donde_termina = indice_inicio + salto_entre_elemento*(tamanio_listas-1)
    while(donde_termina<len(lista)):
        nueva_lista=[]
        for i in range(tamanio_listas):
            nueva_lista.append(lista[(indice_inicio+(salto_entre_elemento*i))])
        if(len(nueva_lista)>0):
            lista_final.append(nueva_lista)
        indice_inicio=indice_inicio+1
        donde_termina = indice_inicio + salto_entre_elemento * (tamanio_listas - 1)
    return lista_final