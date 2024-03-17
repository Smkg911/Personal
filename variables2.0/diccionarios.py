# creando diccionario con (dict)
diccionario = dict(nombre = 'Alejandro', apellido='Espania')

#las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario = {frozenset(['dalto','dario']), 'dato3'}

#creamos un diccionario con valores indefinidos con dict.fromkeys y en las variables se coloca tipo lista para que sean iterables 
diccionario = dict.fromkeys(['nombre', 'apellido', 'suscriptores'])


print(diccionario)