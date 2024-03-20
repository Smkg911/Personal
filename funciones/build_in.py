numeros = [1, 2, 3, 54, 6, 44, 99]

# enconctrando el numero mayor de una lista y el numero mas pequenio
print(max(numeros))
print(min(numeros))

#redondeando a 6 decimales
print(round(50.546461316516323215646652311233213216646, 2))

# retorna false en caso que le demos un 0, vacio, falso, none 
resultado = bool(False)
print (resultado)

# retorna True si todos los valores son verdaderos
resultadoAll = all([254, 'true', 546.41, None])
print(resultadoAll)

#suma todos los valores de un iterable 
sumaTotal = sum(numeros)
print(sumaTotal) 
