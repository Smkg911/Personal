animales = ['gato', 'perro', 'loro', 'hipopotamo', 'pez']
numeros = [10, 62, 12, 72, 1]

# recorriendo la lista animales en bucle con (for in)
for animal in animales:
    print(animal)
    
# recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
# iterando dos listas del mismo tamanio al mismo tiempo con la funcion(zip)
for numero,animal in zip(numeros,animales):
    print(f"recorriendo la lista 1:{numero}")
    print(f"recorriendo la lista 2:{animal}")
    
#le damos un rango de numeros para que se repita, solo numeros
for num in range(1,4):
    print(num)
    
#forma correcta de reccorer una lista con su indice
for num in enumerate(numeros):
    indice = num[0] #[0] significa indice
    valor = num[1] #[1] significa valor 
    print (f"el indice es {indice} y el valor es {valor}")
else: # siempre se va a ejecutar al final del bucle 
    print('el bucle termino')

#todo lo anterior funciona para tuplas y conjuntos