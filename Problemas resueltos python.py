s = "google.com"
ocuTot = {}
#ocuTot ==> es un diccionario con llaves asociadas a un valor :)
#un set ==> Conjunto
#Como te esta creando un conjunto basandose en tu cadena, entonces las letras no se repiten en el conjunto nuevo
miConjunto = list(set(s))
#hago un casting de mi conjunto para convertirlo en una lista para que pueda usar indices con el
for i in range(0,len(miConjunto)):
	ocurrencias = s.count(miConjunto[i])
	ocuTot[miConjunto[i]] = ocurrencias
	#le asigno mi llave que tiene una letra de la palabra y a esa llave le asigno un valor dentro del diccionario :v
print(ocuTot)

