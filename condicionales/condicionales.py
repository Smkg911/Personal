edad = int(input("decime que edad tienes idiota: "))

if edad >= 18:
    print ("buena loko sos mayor de edad ")
else:
    print (" no podes entrar machote")
    
contrasenia_almacenada = "Paparodri02+"
contrasenia = input("ingrese su contrasenia ")

if contrasenia_almacenada == contrasenia:
    print ("podes pasar lokete")
else: 
    print('quien sos vos pelotudito')
    
    
ingresoMensual = int(input ('ingrese su ingreso mensual: '))
gastoMensual = int(input("ingresa tu gasto mensual "))

if ingresoMensual > 10000000:
    if ingresoMensual - gastoMensual < 0:
        print('estas en deficit lokete')
    elif ingresoMensual - gastoMensual > 4000000:
        print('estas bien, segui asi')
    else: 
        print ("estas gastando muchisimo, calmate un poquito")
elif ingresoMensual > 1000000:
    print("estas bien en todos lados pa")
elif ingresoMensual > 100000: 
    print ("te estan robando pa ")


    