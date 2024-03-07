#<<--Como controlar errores en Python-->>#

try:  #El metodo try sirve para comprobar si el codigo tiene algun error
  print(0 / 0)
except ZeroDivisionError as error:  #Es como un "Else" pero con un error que indiquemos
  print("Cannot divide by 0")  #Mensaje que elijamos para el error

try:  #No solo sirve para errores nativos de Python
  assert 1 != 1, "1 es igual a 1"
except AssertionError as error:
  print("1 es igual a 1")

try:  #Se puede usar con nuestros propios condicionales y errores
  age = 10
  if age < 18:
    raise Exception("No se permiten menores de edad")
except Exception as error:
  print(error)

print("Hola")
"""
  Para no tener que escribir un try y un except cada vez
  que queremos confirmar si algun codigo tiene errores o
  si le pusimos condicionales como "Except", lo que
  debemos hacer es hacer un solo try con multiples excepciones
  que nosotros pongamos:

    try:
      print(0 / 0)
      assert 1 != 1, "1 es igual a 1"
      age = 10
      if age < 18:
        raise Exception("No se permiten menores de edad")
    except ZeroDivisionError as error:
      print("Cannot divide by 0")
    except AssertionError as error:
      print("1 es igual a 1")
    except Exception as error:
      print(error)

  Asi evitaremos estar repitiendo bastante codigo
  innecesario y asi tener un script mas limpio, ordenado
  y comprensible para todos los usuarios
"""