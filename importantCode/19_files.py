#<<--Como ejecutar archivos con Python-->>#

file = open("./19_1_filesExample.txt")

print(file.read())  #Leer todo un archivo

print(file.readline())  #Leer solo la linea indicada

for line in file:
  print(line)  #Se puede combinar con bucles

with open("./19_1_filesExample.txt") as file:  #Abrir archivos rapidamente
  for line in file:
    print(line)  #Se puede combinar con bucles
    #Cuando utilizamos "with" no necesitamos cerrar el archivo

file.close() #-> Cerrar el archivo abierto para liberar espacio en memoria