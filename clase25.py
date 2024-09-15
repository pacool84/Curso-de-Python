#Manejo de Archivos CSV

import csv #Esta libreria es la que permite manipular archivos CSV

#Leer un archivo

with open('products.csv', mode='r') as file:
  csv_reader = csv.DictReader(file) #Abrir esta informacion en un formato de "Diccionario", la columna se vuelve la llave em el diccionario
  for fila in csv_reader:
    print(fila)
    
#Mostrar la informacion por columnas

with open('products.csv', mode = 'r') as file:
  csv_reader = csv.DictReader(file)
  for fila in csv_reader:
    print(f'Producto: {fila['name']}, Precio: {fila['price']}')#Se imprime la columna de interes que en este caso es name y price

#Agregar informacion al archivo

new_product = {
  'name': 'ipad',
  'price': '24000',
  'quantity': '10',
  'brand': 'Apple',
  'category': 'Electronics',
  'entry_date': '2025-09-15',
  'total_value': '480000'
}

with open('products.csv', mode = 'a', newline='') as file:
  file.write('\n')#Salto de línea, con esto hacemos que se respete el formato del csv
  csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
  csv_writer.writerow(new_product)