def increment(x):  #Funcion normal
  return x + 1


increment_v2 = lambda x: x + 1  #Funcion Lambda

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

fullname = lambda name, last_name: f"El nombre completo es {name.title()} {last_name.title()}"

userName = fullname("El Tilin", "Insano")
print(userName)
