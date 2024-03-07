#<<<----Map nos sirve para añadir objetos a una lista con lambda----->>>#

numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:  #Metodo comun
  numbers_v2.append(i)

numbers_v3 = list(map(lambda i: i * 2, numbers))  #Metodo con map y lambda

print(numbers)
print(numbers_v2)
print(numbers_v3)

#<<--Sumar dos listas-->>#
nums1 = [1, 2, 3, 4]
nums2 = [34, 12, 10, 99]

result = list(map(lambda x, y: x + y, nums1, nums2))

print("\n")
print(result)