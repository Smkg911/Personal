# creando tupla con tuple() 
tupla = tuple(["dato1", "dato2"])

#se crea una tupla separando cada dato con una coma y si solo se quiere un dato se coloca la coma al final 
tupla = "dato1","dato2"

for tuplo in enumerate(tupla):
    indice = tuplo[0]
    valor = tuplo [1]
    print (f"{indice}:{valor}")

# print(tupla)
print(tupla[1])