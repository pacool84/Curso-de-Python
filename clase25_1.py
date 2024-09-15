# Buenas prácticas al manipular archivos CSV:
# Evitar modificar el archivo original, creando un archivo nuevo con las actualizaciones.
import csv

# Definir rutas para el archivo original y el archivo actualizado.
file_path = 'products.csv'  # Archivo original.
updated_file_path = 'products_updated.csv'  # Nuevo archivo con las actualizaciones.

# Abrir el archivo original en modo lectura ('r').
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)  # Convertir el contenido del archivo CSV a un formato de diccionario.
    
    # Obtener las columnas del archivo original y añadir una nueva columna 'total_value'.
    fieldnames = csv_reader.fieldnames + ['total_value']  # Añadir la columna 'total_value' a las existentes.

    # Abrir el archivo actualizado en modo escritura ('w') para crear el nuevo archivo.
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)  # Preparar el archivo actualizado con las nuevas columnas.
        csv_writer.writeheader()  # Escribir los encabezados (cabeceras de las columnas) en el archivo actualizado.

        # Iterar sobre cada línea del archivo original.
        for linea in csv_reader:
            # Calcular el valor total (precio * cantidad) y agregarlo a la nueva columna 'total_value'.
            linea['total_value'] = float(linea['price']) * int(linea['quantity'])
            csv_writer.writerow(linea)  # Escribir la línea actualizada en el nuevo archivo CSV.