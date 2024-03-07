#<<---Los modulos son funciones que se importan y que nos sirven para programar--->>#

#<--Saber el sistema operativo-->#
import sys

print(sys.path, "\n")

#<--Buscar ciertos caracteres en un string-->#
import re

text = "Mi numero de celular es 311 123 132 34, el codigo del pais es +27, mi numero de la suerte es 19"
result = re.findall("[0-9]+", text)
print(result, "\n")

#<--Revisar el tiempo local y global-->#
import time

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result, "\n")

#<--Contar cantidad de datos repetidos en una lista-->#
import collections

numbers = [1, 2, 3, 10, 6, 2, 7, 4, 9, 4, 7, 2, 46]
counter = collections.Counter(numbers)
print(counter, "\n")