#<<--Manejando iteradores manual y automaticamente-->>#

for i in range(1, 11):
  print(i)

my_iterable = iter(range(1, 11))
print(my_iterable)
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
