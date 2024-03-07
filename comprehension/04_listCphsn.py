#<<<-----Metodos para hacer listas----->>>#

#---> Crear lista de numeros / Metodo normal
numbers = []
for number in range(1, 11):
  numbers.append(number)

print("\nMetodo comun ->", numbers, "\n\n<------------------------------>\n")

#---> Crear lista de numeros / Comprehension - Mas rapido
numbers2 = [number for number in range(1, 11)]

print("Metodo mas eficiente ->", numbers2)

#----->>> Explicacion de como funciona:
"""
  <<<---Explicacion sobre el List Comprehension--->>>
  numbers2 = [] -> Creacion de la lista
  number for number in range(1, 11)

  1. El primer "Element" -> Es el elemento que se añadira a la lista (Es modificable)
  2. For -> El ciclo que se ejecutara
  3. El segundo "Element" -> Este es el elemento que se ejecuta dentro del rango para 
    añadir el primer "Element" a la lista
  4. In -> Es el conector entre el rango y el segundo "Element"
  5. Range -> Este define el rango en el que iterara el segundo "Element"

  Nota -> En el list Comprehension no se debe utilizar el .append ya que este viene
    incluido con el iterador de "For"
"""

#--->>> Fin de la explicacion <<<---#

#----- Creacion de listas con condicionales-----#
print("\n<-----------------# Listas con condicionales #----------------->\n")

#--->> Crear listas con condiciones / Metodo normal
cNumbers = []
for number in range(1, 101):
  if number % 2 == 0:
    cNumbers.append(number * 2)

print("Crear listas con condicionales ->", cNumbers, "\n")

#--->> Crear listas con condiciones / Metodo normal
cNumbers2 = [number * 2 for number in range(1, 101) if number % 2 == 0]
print("Crear listas con condicionales y Comprehension ->", cNumbers2, "\n")
