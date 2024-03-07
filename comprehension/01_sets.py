import random  #Generador de numeros aleatorios

print("." * 94)

#<---Metodos para hacer diccionarios con condiciones--->#
persons = ["Samuel", "Kevin", "David", "Julian", "Nicolas"]

personsAge = {person: random.randint(10, 30) for person in persons}
print("\nEdad de personas:", personsAge)

print("\n\n\n░▒▓▒░▒▓▒░ Verificacion de edad ░▒▓▒░▒▓▒░")

print("\n<<--La edad debe ser mayor o igual a 18 para ingresar al bar-->>\n\n")

personsAccepted = {
    person: age
    for (person, age) in personsAge.items() if age >= 18
}
print("\nPersonas aceptadas:", personsAccepted)

personsDenied = {
    person: age
    for (person, age) in personsAge.items() if age < 18
}
print("\nPersonas denegadas:", personsDenied, "\n")

print("." * 94)

#<<-----Iteracion de textos con diccionarios----->>#
text = "Programar en Python con Platzi es muy divertido!"
print("\nTexto normal:", text)

textUpperVowels = {c: c.upper() for c in text if c in "aeiou"}
print("\nTexto con las vocales en MAYUSCULA:", textUpperVowels)

textCountVowels = {c: text.count(c) for c in text if c in "aeiou"}
print("\nContador de vocales:", textCountVowels)
