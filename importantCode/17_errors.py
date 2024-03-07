#<<--Manejo de errores-->>#
"""
  print(10 / 0) #Error de division por 0

  print(result)  #Error de llamar una variable no definida

  suma = lambda x, y: x * y
  assert suma(2, 2) == 4  #Error de comprobacion de valores fallida
"""

age = 10
if age < 18:
  raise Exception("Debes ser mayor de edad")  #Lanzar un error que definamos