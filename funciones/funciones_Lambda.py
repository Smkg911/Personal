numeros = [1,2,3,4,5,6,7,8,9]

#crea funciones anonimas
mulriplicarPorDos = lambda x : x*2

# #creando funcion comun que diga si es par o no
# def es_par(num):
#     if (num % 2 == 0):
#         return True
    
# #usando filter con una funcion comun 
# numerosPares = filter(es_par,numeros)

#creando lo mismo de antes pero con lambda
numerosPares = filter(lambda numero : numero % 2 == 0, numeros)#ejecuta cada valore de un iterable (filter)

print(list(numerosPares))