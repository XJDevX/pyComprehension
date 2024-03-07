import random  #Generador de numeros aleatorios

#<<<---Metodos para hacer diccionarios--->>>#
print("." * 94)

#---> Crear diccionarios / Metodo normal
dict1 = {}
for element in range(1, 5):
  dict1[element] = element * 3

print("\nDiccionario con el metodo normal ->", dict1)

#---> Crear diccionarios / Metodo Rapido - Comprehension
dict2 = {element: element * 3 for element in range(1, 5)}

print("\nDiccionario con el metodo Comprehension ->", dict2, "\n")

###Separador###

print("." * 94)

###Fin del separador###

#---> Otro ejemplo para crear diccionarios

#-> Metodo normal
dictCountries = {"Colombia", "Peru", "Brasil"}
population = {}
for country in dictCountries:
  population[country] = random.randint(1000000, 100000000)

print("\nDiccionario con poblacion del pais - Metodo normal ->", population)

#-> Metodo rapido - Comprehension
population2 = {
    country: random.randint(1000000, 100000000)
    for country in dictCountries
}

print("\nDiccionario con poblacion del pais - Metodo Comprehension ->",
      population2, "\n")

#----->>> Explicacion de como funciona:
"""
  <<<---Explicacion sobre el List Comprehension--->>>
  population2 = {} -> Creacion del diccionario
  country: random.randint(1000000, 100000000) for country in dictCountries

  1. El primer "Country" -> Es el elemento que se añadira al diccionario (Es modificable)
  2. Random.randint() -> Generador de numeros aleatorios enteros
  3. For -> Iterador para añadir el elemento
  4. El segundo "Country" -> Es el elemento al cual se le agregara la caracteristica
  5. In -> Indica el rango
  6. dictCountries -> Indica de donde sera elegido el segundo "Country"

"""

#--->>> Fin de la explicacion <<<---#

print("." * 94)

#-----Nota-----#
names = ["Julian", "Tomas", "Samuel"]
ages = [24, 19, 38]

print("\nComo ***IMPRIMIR*** un diccionario a partir de 2 listas ->", names,
      ages)
print("\n", list(zip(names, ages)), "\n")  #Crear un dicciorario con 2 listas

touristicSites = ["Torre Eiffel", "Burj Kalifa", "Cristo Redentor"]
locations = ["Francia", "Emiratos Arabes Unidos", "Brasil"]

sitesInfo = {
    touristicSite: location
    for (touristicSite, location) in zip(touristicSites, locations)
}

print("\nComo ***CREAR*** un diccionario a partir de 2 listas", touristicSites,
      locations)
print(sitesInfo, "\n")

print("." * 94)
