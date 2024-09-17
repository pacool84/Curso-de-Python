# Análisis de datos de ventas:
# Identificación de tendencias y patrones en los números usando estadística descriptiva.

import statistics  # Importamos la librería 'statistics' para realizar cálculos estadísticos.
import csv  # Importamos la librería 'csv' para leer archivos CSV.

# 1. Lectura de las ventas mensuales desde un archivo CSV:
# Creamos un diccionario 'monthly_sales' donde las claves son los meses y los valores son las ventas.
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)  # Leemos el archivo como diccionario, donde cada fila es un diccionario.
    for linea in reader:
        month = linea['month']  # Extraemos el mes.
        sales = int(linea['sales'])  # Convertimos las ventas a entero.
        monthly_sales[month] = sales  # Asignamos el mes como clave y las ventas como valor en el diccionario.

# 2. Extraer las ventas para su análisis:
# Convertimos los valores del diccionario a una lista para realizar operaciones estadísticas.
sales = list(monthly_sales.values())  # Extraemos los valores (ventas) y los guardamos en una lista.
print(sales)

# 3. Cálculo de la media (promedio):
# La media se obtiene sumando todas las ventas y dividiéndolas entre el número total de meses.
mean_sales = statistics.mean(sales)
print(f"La media de ventas es: {mean_sales}")

# 4. Cálculo de la mediana:
# La mediana es el valor que divide a la lista de ventas en dos partes iguales.
median_sales = statistics.median(sales)
print(f"La mediana de ventas es: {median_sales}")

# 5. Cálculo de la moda:
# La moda es el valor que más se repite en la lista de ventas.
mode_sales = statistics.mode(sales)
print(f'La moda de ventas es: {mode_sales}')

# 6. Cálculo de la desviación estándar:
# La desviación estándar mide la dispersión de las ventas respecto a la media.
stdev_sales = statistics.stdev(sales)
print(f"La desviación estándar de ventas es: {stdev_sales}")

# 7. Cálculo de la varianza:
# La varianza mide cuánto varían las ventas respecto a la media.
variance_sales = statistics.variance(sales)
print(f"La varianza de ventas es: {variance_sales}")

# 8. Cálculo del máximo y mínimo de ventas:
# Encontramos los valores máximos y mínimos de ventas.
max_sales = max(sales)
min_sales = min(sales)

# 9. Cálculo del rango de ventas:
# El rango es la diferencia entre las ventas máximas y mínimas.
range_sales = max_sales - min_sales
print(f'El rango de ventas es: {range_sales}')