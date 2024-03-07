import random  #Generador de numeros aleatorios


#<<---Como crear funciones--->>#
def suma(a, b):
  result = a + b
  print(f"\nLa suma entre {a} y {b} es:", result, "\n")


suma(19, 81)  #Suma numeros definidos

suma(random.randint(1, 100), random.randint(1, 100))  #Suma numeros aleatorios
"""
  Como funciona? -> 
    def -> Es el que define la funcion
    "suma" o "Nombre de la funcion" -> define como se ejecutara la funcion
    () -> Definene parametros para ejecutar la funcion
"""