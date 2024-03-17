minimoH = 2.5
promedioH = 4
maximoH = 7
crudoPromedio = 5
cursoDalto = 1.5 
crudoDalto = 3.5

# difirencia con duracion 
diferenciaMin = 100 - cursoDalto / minimoH *100
diferenciaPromedio = 100 - cursoDalto / promedioH * 100
diferenciaMax = 100 - cursoDalto *1000 // maximoH / 10 

print (f"el curso de dalto es un {diferenciaMin}% mas rapido que el mas rapido")
print (f"el curso de dalto es un {diferenciaMax}% mas rapido que el mas lento")
print (f"el curso de dalto es un {diferenciaPromedio}% mas rapido que el mas promedio")

print("------------------------------------------------------") 
# crudos 
basuraDalto = 100 - cursoDalto * 1000 // crudoDalto / 10 
basuraOtros = 100 - promedioH * 1000 // crudoPromedio / 10

print("------------------------------------------------------") 
print(f"esta es la basura de dalto {basuraDalto}")
print(f"esta es la basura de los cursos basura {basuraOtros}")

# diferencia de los cursos si los cursos duraran 10 horas
print("------------------------------------------------------") 

print (f"mirar 10 horas de este curso equivalen a ver {promedioH *100 // cursoDalto / 10}horas de otro curso ")
print (f"mirar 10 horas de otros cursos equivalen a ver {cursoDalto *100 // promedioH / 10}horas del curso de dalto ")
