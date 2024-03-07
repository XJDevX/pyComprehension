#<--Reduce, hacer una reduccion de una lista en un solo valor-->#

import functools

numbers = [1, 2, 3, 4]


def acumulate(n, item):
  print(f"Counter -> {n}")
  print(f"Item -> {item}")
  print(f"Suma -> {n} + {item}\n")
  return n + item


result = functools.reduce(acumulate, numbers)

print(f"Resultado de la acumulacion -> {result}")