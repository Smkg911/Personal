# lista, si se pueden modificar elementos (list)
lista = ["soy mario", "tu mama", 5468213, True, False, 20.874]

# creanto una tupla, no se pueden modificar elementos (tuple), pero si se puede reconstruir 
tupla = ("soy mario", "tu mama", 5468213, True, False, 20.874)

# modifica el dato señalado en la lista ([variable])
lista[2] = "tomamama"

# la tupla no se puede modificar 
# tupla[2] = True

# creando un conjunto (set), no se pueden modificar elementos, pero si se puede reconstruir, no se puede acceder a indices especificos , tampoco permite repetir valores 
conjunto = ["soy mario", "tu mama", 5468213, True, False, 20.874]

#creando un diccionario (dict) = KEY : value,  
diccionario = {
        'nombre' : "saul mario",
        'edad' : 45,
        'motivo' : "aprender",
        'esta emocionado' : True,
        'datoDuplicado' : "saul mario"
    
}

print(diccionario)