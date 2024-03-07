#<<---"Return" y su uso en las funciones--->>#
print("." * 94)


#--->Devolviendo un "Print" por defecto
def autoSumRange(min, max):
  result = 0
  for x in range(min, max):
    result += x
  print(f"\nLa auto suma desde {min} hasta {max} es: {result}\n")


autoSumRange(1, 15)  #--->Solo para cuando no se necesita guardar el resultado

print("." * 94, "\n")


#--->Devolviendo un valor para almacenar en una variable con "Return"
def autoSumRangeVar(min, max):
  result = 0
  for x in range(min, max):
    result += x
  return result


print("Cuanto es la autosuma entre 1 y 45?")
answer = autoSumRangeVar(1, 45)

print(f"La autosuma entre 1 y 45 es: {answer}\n")

#<<---Fin del programa--->>#

print("." * 94)