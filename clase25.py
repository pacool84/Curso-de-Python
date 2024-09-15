# Manejo de Archivos CSV en Python

import csv  # La librería 'csv' permite leer, escribir y manipular archivos en formato CSV.

# 1. Leer un archivo CSV:
# Abrimos el archivo 'products.csv' en modo lectura ('r').
# DictReader permite leer el archivo CSV y convertir cada fila en un diccionario, donde las llaves son los nombres de las columnas.
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)  # Convierte cada fila del CSV en un diccionario, usando las cabeceras como llaves.
    for fila in csv_reader:
        print(fila)  # Imprime cada fila del CSV en formato de diccionario.

# 2. Mostrar información específica por columnas:
# En este caso, queremos mostrar solo los nombres de productos y sus precios.
# DictReader permite acceder a las columnas usando las llaves del diccionario, que corresponden a las cabeceras del CSV.
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for fila in csv_reader:
        # Usamos las llaves 'name' y 'price' para obtener el nombre y precio de cada producto.
        print(f'Producto: {fila["name"]}, Precio: {fila["price"]}')  # Mostramos solo la columna "name" y "price".

# 3. Agregar información a un archivo CSV (modo 'a' para append):
# Definimos un nuevo producto con sus respectivos campos (coinciden con las columnas del CSV).
new_product = {
    'name': 'ipad',
    'price': '24000',
    'quantity': '10',
    'brand': 'Apple',
    'category': 'Electronics',
    'entry_date': '2025-09-15',
    'total_value': '480000'
}

# Abrimos el archivo en modo append ('a') para añadir la nueva fila sin modificar las existentes.
# newline='' asegura que no se agreguen líneas en blanco adicionales en algunos sistemas.
with open('products.csv', mode='a', newline='') as file:
    file.write('\n')  # Añadimos un salto de línea para asegurar que el formato del CSV se mantenga.
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())  # DictWriter prepara el archivo para escribir diccionarios.
    csv_writer.writerow(new_product)  # Añadimos el nuevo producto como una nueva fila en el archivo CSV.