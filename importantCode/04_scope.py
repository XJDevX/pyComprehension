print("El contenido de este script es mas detallado en el codigo")

#<<-----Tipos de alcanze de variables o Scope----->>#
text = "Estoy programando en Python!"  #---> Variable global


def sum(a, b):
  result = a + b  #---> La variable "Result solo puede ser usada dentro de la funcion"
  return result


result = sum(8, 9)  #---> A menos de que sea definida como una variable global
"""
  Tipos de alcanze de variables:
    -Alcanze local: Este alcanze solo cubre en la seccion en la que esta como una
    funcion, lo que significa es que esta variable fuera de la funcion no se podra   
    usar debido a que no tiene el suficiente alcanze para operar en todo el archivo

    -Alcanze global: Este alcanze cubre todo el archivo, lo que significa que en   
    TODAS las secciones del archivo se podra utilizar, como son las funciones o 
    condicionales
"""