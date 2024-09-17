# Manejo de archivos JSON con Python:
# JSON (JavaScript Object Notation) es un formato común para almacenar y transferir datos entre aplicaciones web.

import json  # Importamos la librería 'json' para manejar archivos en formato JSON.

# 1. Lectura de un archivo JSON:
# Abrimos el archivo 'products.json' en modo lectura ('r').
# json.load() convierte el contenido del archivo JSON en un objeto Python (en este caso, una lista de diccionarios).
with open('products.json', mode='r') as file:
    products = json.load(file)  # Cargamos los datos del archivo JSON y los convertimos a un objeto Python (lista de productos).

# 2. Mostrar el contenido del archivo JSON:
# Iteramos sobre la lista de productos, accediendo a los valores de las llaves 'name' y 'price'.
for producto in products:
    # Accedemos a cada diccionario (producto) y mostramos sus atributos específicos.
    print(f"Producto: {producto['name']}, Precio: ${producto['price']}")  # Mostramos el nombre y el precio de cada producto.

# 3. Añadir información al archivo JSON:
# Definimos un nuevo producto con las mismas llaves que los productos existentes.
new_product = {
    'name': 'ipad',
    'price': '24000',
    'quantity': '10',
    'brand': 'Apple',
    'category': 'Electronics',
    'entry_date': '2025-09-15',
    'total_value': '480000'
}

# 4. Actualización del archivo JSON:
# a. Abrimos el archivo en modo lectura ('r') para cargar los datos actuales.
with open('products.json', mode='r') as file:
    products = json.load(file)  # Cargamos los productos actuales del archivo JSON.

# b. Añadimos el nuevo producto a la lista existente.
products.append(new_product)  # Usamos append() para agregar el nuevo producto a la lista de productos.

# c. Escribimos la lista actualizada nuevamente en el archivo JSON:
# Abrimos el archivo en modo escritura ('w') para sobreescribir el archivo con los datos actualizados.
with open('products.json', mode='w') as file:
    # Usamos json.dump() para escribir los datos actualizados en el archivo.
    # El parámetro 'indent = 4' se usa para formatear el archivo con una sangría de 4 espacios, mejorando la legibilidad.
    json.dump(products, file, indent=4)  # Sobrescribimos el archivo con la lista actualizada de productos.