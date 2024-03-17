diccionario = {
    'nombre' : "raul",
    'apellido' : "salinas",
    'altura' : 1.78
}
#recorriendo un diccionario con items para obtener las keys 
for datos in diccionario:
    print (datos)
    
#recorriendo un diccionario con items para obtener las keys y los values
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print (f"la key es: {key} y el value es: {value}")