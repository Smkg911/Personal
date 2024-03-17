# creando un conjunto con (set)
conjunto = set(["dato1", "dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto2 = frozenset({"dato2", "dato3"})# con (frozenset) podemos meter conjuntos dentro de otros conjuntos
conjunto1 = {conjunto2, "dato2"}
print(conjunto1)

#teoria de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# (issubset) = subconjunto o <=
resultado = conjunto2 .issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# (issuperset) = superconjunto o >=
resultado2 = conjunto1.issuperset(conjunto2)
resultado2 = conjunto1 >= conjunto2

# verificar si hay un dato en comun (isdisjoint)
resultado3 = conjunto2.isdisjoint(conjunto1) # solo es True solo cuando los conjuntos que se estan comparando son distintos

print(resultado)
print(resultado2)
print(resultado3)