import utils

#<<--Aqui veremos como llamar a otros modulos a python-->>#
"""
  Los modulos son archivos de Python que se pueden iterar dentro de otros
  archivos, esto permitiendonos tener un mayor orden en el proyecto
"""

data = [{
    "Country": "Colombia",
    "Population": 300
}, {
    "Country": "Bolivia",
    "Population": 200
}]


def run():
  keys, values = utils.get_population()
  print(keys, values)

  print(utils.Name)

  country = input("Digite el pais -> ")

  print(utils.population_by_country(data, country))


if __name__ == "__main__":
  run()