#forma no optima de sumar valores 
# def suma(lista):
#     numerosSumados = 0
#     for numeros in lista:
#         numerosSumados = numerosSumados + numeros
#     return numerosSumados
# resultado = suma([5, 3, 5, 8, 8, 10, 20])

#utilizando el parametro (args)
def suma(nombre,*numeros): # despues del (*), todo se convierte en una lista 
    return f'{nombre}, el resultado de tu suma es {sum(numeros)}'

resultado = suma('Samuel',4,5,6,7,9)
print(resultado)