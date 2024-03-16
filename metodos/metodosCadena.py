cadena1 = "hola loquete"
cadena2 = "464646546547"
cadena3 = "holamaquinasoydalto"

#nos muestra los metodos o comandos posibles para cada dato (dir)
posibilidades = dir(cadena1)

#convierte todo a mayusculas (upper)
mayusc = cadena1.upper()

#convierte todo a minusculas (lower)
minusc = cadena1.lower()

#convertimos la primera letra en mayucula (capitalize)
pMayus = cadena1.capitalize()

# busca una cadena en otra cadena(find)
busqueda = cadena1.find("a") # si no encuentra nada nos devuelve -1

#busca una cadena dentro de otra cadena (index)
busqueda2 = cadena1.index("a") # si no encuentra nada nos tira un error 

#si es numerico devuelve True si no es numerico devuelve False (isnumeric)
numerico = cadena2.isnumeric()

#si es alfanumerico devuelve True si no lo es devuelve False
alfaNumerico = cadena3.isalpha() 

#busca una cadena dentro de otra cadena (count) devuelve el numero de coincidencias
coincidencia = cadena1.count("a") #si no encuentra devuelve 0

# cuenta la cantidad de caracteres(len) en una funcion, no un metodo
caracteres = len(cadena3)

#verifica si una cadena empieza con una cadena dada, si es asi devuelve True (starswith) 
empieza = cadena1.startswith("hola ")

#verifica si una cadena termina con una cadena dada, si es asi devuelve true (endswith)
termina = cadena1.endswith("loquete")

#remplaza un pedazo de la cadena dada por otra dada (replace)
remplaza1 = cadena1.replace("loquete", "machote") #si no encuentra coincidencia no se remplaza nada 

#separar cadenas con la cadena que le pasemos (split)
separar = cadena1.split(" ")

print(separar)