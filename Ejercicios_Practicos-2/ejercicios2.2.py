#creando una funcion que nos devuelva los numeros primos entre el 0 y el argumento que pasamos

#se crea una funcion que verifica si es un numero primo o no
def esPrimos(num):
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        if num % i == 0: return False
    #si termina el bucle significa que no pudo dividirse por lo tanto es primo 
    return True
        
#creamos una funcion que retorna una lista con todos los primos
def primosHasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = esPrimos(i)
        #en caso de que sea primo lo agregamos a la lista
        if resultado == True: primos.append(i)
        
        #devolvemos la lista
    return primos

resultado = primosHasta(13)
print(resultado)