#---Set es lo mismo que Conjunto---#

#<<<-----Operaciones con conjuntos----->>>#
set_a = {"Colombia", "Mexico", "Bolivia"}
set_b = {"Peru", "Bolivia"}
print("Operaciones de conjuntos")
print("Conjunto A ->", set_a)
print("Conjunto B ->", set_b, "\n")

#Unir dos conjuntos / Union
set_c = set_a.union(set_b)  #Union de conjuntos desde una variable
print("Union de dos conjuntos desde una variable ->", set_c)

nextPrintText = "Union de dos conjuntos desde un print ->"
print(nextPrintText, set_a | set_b, "\n")  #Union de conjuntos desde un print

#Intersecar dos conjuntos / Interseccion
set_c = set_a.intersection(
    set_b)  #Interseccion de conjuntos desde una variable
print("Interseccion de dos conjuntos desde una variable ->", set_c)

nextPrintText = "Interseccion de dos conjuntos desde un print ->"
print(nextPrintText, set_a & set_b,
      "\n")  #Interseccion de conjuntos desde un print

#Diferencia entre dos conjuntos / Diferencia
set_c = set_a.difference(set_b)  #Diferencia de conjuntos desde una variable
print("Diferencia de dos conjuntos desde una variable ->", set_c)

nextPrintText = "Diferencia de dos conjuntos desde un print ->"
print(nextPrintText, set_a - set_b,
      "\n")  #Diferencia de conjuntos desde un print

#Diferencia simetrica entre dos conjuntos / Diferencia simetrica
set_c = set_a.symmetric_difference(set_b)
print("Diferencia simetrica de dos conjuntos desde una variable ->", set_c)

nextPrintText = "Diferencia simetrica de dos conjuntos desde un print ->"
print(nextPrintText, set_a ^ set_b, "\n")  #Diferencia simetrica desde un print
