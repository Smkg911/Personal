lista = [27, 548216, 556161, False, True]

# develve la cantidad de elementos de la lista (len)
resultado = len(lista)

#agregando un elemento a la lista (append)
lista.append(1)

#agregando un elemento a la lista en un indice especifico (insert)
lista.insert(2, 4581554)

#agregando varios elemento a la lista dentro de los corchetes (extend)
lista.extend([False, 2030])

#eliminando un elemento de la lista por indice (pop)
lista.pop(0) # -1 para eliminar el ultimo y asi sucesivamente  

#elimina un elemento de la lista por su valor (remove)
lista.remove(4581554)

#elimina todos los elementos de la lista (clear)
# lista.clear()

#ordena los elementos de forma acendente (sort), no permite cadenas de texto
lista.sort()#  si aplicamos el parametro reverse = true se invierte al ordenar 

#invirtiendo los elementos de una lista (reverse)
lista.reverse()

# verificando si un elemento completos que se encuentra en la lista (index), retorna el indice del elemento dentro de la lista (index)
elementoEncontrado = lista.index(False) 
#en caso de que se quiera buscar algo dentro de un rango en especifico se lo toma de la siguiente manera : lista.index(valorBuscado,rangoInicial,RangoFinal)

'''--------------------------------------------------------------------------------------------------------------------------
# Agregado teacher Daniel 
-----------------------------------------------------------------------------------------------------------------------------'''

#verifica cuantas veces se repite un elemento dentro de la lista, en caso de que no encuentre una coincidencia retorna (0), (count)
elementosIguales = lista.count(0)

#sirve para copiar los elementos de una lista a otra (copy)
lista2 = lista.copy()
'''_________________________________________________________________________________________________________________________
#distintos operadores
____________________________________________________________________________________________________________________________'''
# (is) verifica si los los elementos son iguales y para lo contrario se utiliza un (not) despues de la declaracion del (is)
a = lista2 is lista
b = lista is not lista2

print(a)
print(b)

# (in) verifica si un elemento se encunetra dentro de de una lista, retorna un booleano
c = True in lista # para lo contrario se utiliza un (not) despues de la declaracion del (is)

print(c)
print(lista)
print(lista2)
