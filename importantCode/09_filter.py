#<<--Los filtros se pueden añadir a listas-->>#

numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Lista completa: {numbers}")
print(f"Solo pares (Filtro): {new_numbers}")

#-->Sintaxis mas sencilla para un filtro
