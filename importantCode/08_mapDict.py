#<<--Como usar map con diccionarios-->>#

stock = [{
    "product": "camisa",
    "price": 25,
}, {
    "product": "pantalon",
    "price": 50
}, {
    "product": "saco",
    "price": 40
}]

prices = list(map(lambda item: item["price"], stock))
print(prices)


def addTaxes(item):
  localitems = item.copy()
  localitems["taxes"] = item["price"] * .19
  return localitems


new_items = list(map(addTaxes, stock))
print(f"Lista nueva:\n{new_items}")
print(f"Lista antigua:\n{stock}")