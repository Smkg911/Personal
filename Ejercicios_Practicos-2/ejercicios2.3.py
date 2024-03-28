#creando una funcion que nos devuelve la serie fibonacci entre el 0 y el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacciLista = [0]
    for i in range(num):
        if b > num: return fibonacciLista
        else:
            fibonacciLista.append(b)
            a,b = b, a+b
        
resultado = fibonacci(1597)
print(resultado)