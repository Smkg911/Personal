lista = list([27, 548216, 556161, False, True])

# develve la cantidad de elementos de la lista 
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

# verificando si un elemento completos que se encuentra en la lista (index)
elementoEncontrado = lista.index(False)


print(elementoEncontrado)