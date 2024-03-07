#---Conjuntos y Set son lo mismo---#

#<<<-----Metodo CRUD con los Conjuntos----->>>#
set_countries = {"Colombia", "Ecuador", "Peru", "Chile", "Venezuela"}
print("Conjunto de paises ->", set_countries, "\n")

#---Longitud de un Conjuntos
set_countriesSize = len(set_countries)
print("Longitud de elementos del Conjunto ->", set_countriesSize, "\n")

#---Cuantos elementos de cierto tipo tiene un conjunto
print("'Colombia' esta en el conjunto? ->", "Colombia" in set_countries)
print("'E.E.U.U.' esta en el conjunto? ->", "E.E.U.U." in set_countries, "\n")

#---Agregar elementos a un Conjunto / Create
set_countries.add("Brasil")
print("('Brasil') fue añadido al Conjunto ->", set_countries, "\n")

#---Actualizar un elementos en un Conjunto / Update
set_countries.update({"Argentina", "Mexico", "Uruguay"})
print("('Argentina', 'Mexico', 'Uruguay') fueron actualizados ->",
      set_countries, "\n")

#---Eliminar elementos de un Conjunto / Delete
set_countries.remove(
    "Mexico")  #Si el elemento no existe pone un codigo de error
print("('Mexico') fue eliminado del Conjunto ->", set_countries)

set_countries.discard("Ecuador")  #Si el elemento no existe no pone error
print("('Ecuador') fue eliminado del Conjunto ->", set_countries, "\n")

#---Eliminar todo un Conjunto / Clear
set_countries.clear()
print("Conjunto vacio ->", set_countries)
