# #creando una funcion de tres parametros 
# def frase(nombre, apellido,adjetivo):
#     return f'hola {nombre} {apellido}, sos muy {adjetivo}'

# #utilizando keywords arguments
# fraseResultado = frase(adjetivo = "capo", nombre = "Alejandro", apellido = "Espania")
# print(fraseResultado)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido,adjetivo = "Tonto"):
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

fraseResultado =frase('lucas','dalto')
print (fraseResultado)
