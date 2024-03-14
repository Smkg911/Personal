diccionario = {
    "nombre" : 'sapo', 
    "apellidos" : 'sepia', 
    "dinero" : 15151515515     
}

#nos devuelve un objeto dict_item (que se puede cambiar)
claves = diccionario.keys()

#obteniendo un elemento con (get),si no tiene la key no lanza un eror 
obtener = diccionario.get("dinero")

#elimina todos los elementos del diccionario (clear)
# diccionario.clear()

#elimina un elemento del diccionario (pop)
diccionario.pop("nombre")#pala eliminar mas de un elmento se pone , y el nombre 

#obteniendo un elemento dict_item iterable (items)
diccionarioIterable = diccionario.items()


print(diccionarioIterable)