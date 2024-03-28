#faltarosn los profes y los pibes van a armar la clase

#funcion para obtener al asistente y al profesor segun el rango de edad
def obtenerCompanieros(cantidad):
    
    #creando una lista con los companieros
    companieros = []
    
    #ejecutando un for para pedir informacion de cada companiero
    for i in range(cantidad): #range le da un rango de repeticiones al bucle
        nombre = input ('ingrese el nombre del companiero ')
        edad = int(input('ingrese la edad del companiero '))
        companiero = (nombre, edad)
        
        #agregando la informacion a la lista (append)
        companieros.append(companiero)
    
    #ordenandolos de menor a mayor segun la edad
    companieros.sort(key = lambda x : x[1])
    
    #companieros[x] devuelve una tupla con los indices (nombre,edad) y con el segundo [x] devolvemos el valor indicado dentro de la tupla
    #definimos al asistente y al profesor
    asistente = companieros[0][0]
    profesor = companieros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos la tupla que nos retorna la funcion
asistente,profesor = obtenerCompanieros(5)
#mostramos el resultado
print(f"el asistente es {asistente}, y el profesor es {profesor}")
