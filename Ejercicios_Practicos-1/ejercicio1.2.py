palabraUsuario = input("porfavor inserte su palabra ")
palabrasTotal = len(palabraUsuario.split(" "))

print (f"dijiste {palabrasTotal} palabras")

tiempo = palabrasTotal / 2
if tiempo > 60:
    print("tampoco te dije que escribieras una biblia manito")
else:
    print(f"te vas a demorar {tiempo} segundos flaco")
    
print(f"dalto la dijo en {palabrasTotal / 2 * 1.3} segundos")