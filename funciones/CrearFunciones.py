#creando una funcion simple
def saludar():
    print('hola lucas mi maestro')
    
# ejecutando la funcion simple     
saludar()

#creando una funcion con parametros
def saludar2(nombre,sexo):
    sexo = sexo.lower()
    if sexo == 'mujer':
        adjetivo = 'reina'
    elif sexo == 'hombre':
        adjetivo = 'titan'
    else: 
        adjetivo = 'estupido'
    print(f'hola {nombre}, mi {adjetivo} como andas')
    
saludar2('marcos', 'hombre')
saludar2('Andrea', 'MujEr')
saludar2('matias','fluido')

#crar una funcion que nos retorne varios valores
def crearContraseniaRandom(num):
    chars = 'abcdefghijklmndkljglfjksgjkhsdjklhgkhdfghslfghsdkjfhgskjdghskjopq'
    value = str(num)
    num = int(value[0])
    c1 = num  + 2
    c2 = num - 2
    c3 = num 
    c4 = num * 3
    contrasenia = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{num *2}"
    return contrasenia, num

#desempaquetando la funcion
pasword,PrimerNumero = crearContraseniaRandom(9) 

#mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f'tu contrasenia es: {pasword}')
print(f'el numweo utiizado para tu contrasenia fue: {PrimerNumero}')