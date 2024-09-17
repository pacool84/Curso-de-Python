#Manejo archivos JSON con python 
#Es util para manejar datos con aplicaciones WEB
import json

#Lectura del archivo
with open('products.json', mode = 'r') as file:
  products = json.load(file)#Con esto tenemos la lectura de archivos

#Mostrar el contenido del archivo
for producto  in products:
  #Iteramos por cada uno de los productos 
  #print(producto)
  #Iterando por cada una de las llaves / key que queramos
  print(f"Producto: {producto['name']}, Precio ${producto['price']}")

#Añadir informacion al archivo JSON

file_path = 'products.json'

new_product = {
    'name': 'ipad',
    'price': '24000',
    'quantity': '10',
    'brand': 'Apple',
    'category': 'Electronics',
    'entry_date': '2025-09-15',
    'total_value': '480000'
}

#Abrimos en modo lectura
with open(file_path, mode = 'r') as file:
  products = json.load(file)
  
products.append(new_product)

with open(file_path, mode = 'w') as file:
  json.dump(products, file, indent = 4)