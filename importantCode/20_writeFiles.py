#<<--Como modificar archivos desde codigo en Python-->>#

with open("./19_1_filesExample.txt", "r+") as file:  #Modificar archivos
  for line in file:  #El permiso "r+" nos permite modificar el archivo sin reemplazarlo
    print(line)
  file.write("\nEste es una modificacion externa del archivo")
  file.write(", Esto lo aprenderas mas adelante en el curso")

#Otra manera del codigo anterior:
"""
  En este codigo lo que estariamos haciendo es que estariamos reescribiendo todo
  el archivo segun lo que hayamos añadido en nuestro codigo, esta linea se puede
  ejecutar cambiando el permiso de "r+" por "w+":
  
    with open("./19(1)_filesExample.txt", "2+") as file:  #Modificar archivos
      for line in file:  #El permiso "w+" permite modificar el archivo reemplazandolo
        print(line)
      file.write("\nEste es una modificacion externa del archivo")
      file.write(", Esto lo aprenderas mas adelante en el curso")

  Hay que tener mucho cuidado con este permiso ya que podriamos estar modificando y
  eliminando informacion confidencial o muy importante que se encuentre en ese archivo
"""