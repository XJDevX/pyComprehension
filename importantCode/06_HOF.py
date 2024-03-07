#<<<-----Higher Order Function----->>>#

#-> Esto significa que usaremos una funcion dento de otra


#<<<---Funciones normales (Un poco mas extenso)--->>>#
def increment(x):
  return x + 1


def hof(x, func):
  return x + func(x)


result = hof(14, increment)  #-> Esto es igual a (14 + (14 + 1))
print(result, "\n")

#<<<---Funciones lambda (Una sintaxis mas corta)--->>>#
increment_v2 = lambda x: x + 1

hof_v2 = lambda x, func: x + func(x)

result_v2 = hof_v2(19, increment_v2)
print(result_v2)

#<<<---Funciones de lambda (Sintaxis definitiva))--->>>#
hof_v3 = lambda x, func: x + func(x)

result_v3 = hof_v3(19, lambda x: x / 2)  #Se puede cambiar por la misma lambda
print(result_v2)