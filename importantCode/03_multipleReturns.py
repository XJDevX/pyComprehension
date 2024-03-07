print("." * 94)


#<<-----Los "Return" se pueden devolver mas que solo 1 segun los parametros----->>#
def volumeOfASolid(lenght, widht, depth):
  result = lenght * widht * depth
  return result, "Platzi", True


print("\nCual es el volumen de un cubo de 5cm?")
answer = volumeOfASolid(5, 5, 5)

print(f"El volumen de un cubo de 5cm es de: {answer}\n")
"""
  Nota importante
  -Si al definir la funcion en los parametros pones un igual, ese sera 
  el valor por defecto y si al ejecutar la funcion no se llama alguno de
  los parametros estos seran asignados con el valor por defecto:
    ┌────────────────────────────────────────────────────┐
    │def volumeOfASolid(lenght = 1, widht = 1, depth = 1)│
    └────────────────────────────────────────────────────┘
"""

#<<--Fin del programa-->>#
print("." * 94)