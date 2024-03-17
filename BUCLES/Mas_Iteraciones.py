frutas = ['granadas', 'naranjas', 'peras', 'uvas', 'ciruela','durazno']

for fruta in frutas:
    if fruta == 'granadas':
        continue #salta el elemento propuesto en el if con la sentencia (continue)
    print(f"Me voy a comer una {fruta}")
    
print('---------------------------------------------')

#evitar que el bucle siga ejecutandosen (break), (el else no se ejecuta tampoco)
for fruta in frutas:
    if fruta == 'peras':
        break 
    print(f"Me voy a comer una {fruta}")
    
#recorrer un cadena de texto 
cadena = "hola maestro como estas"

for letra in cadena:
    print(letra)
    
#bucle for en una sola linea de codigo  (duplicamops los numeros)
numeros = [2, 3, 5, 10]

numerosDuplicaos = [x*2 for x in numeros]
print(numerosDuplicaos)