#<--Como importar paquetes o carpetas con scripts-->#

#-->Es necesario crear un archivo __init__ para importar paquetes automaticamente
"""
from Packages.mod_1 import func_1, func_2
from Packages.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())
"""

import Packages_14

print(Packages_14.URL)
print(Packages_14.mod_1.func_1())