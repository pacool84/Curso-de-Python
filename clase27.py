#Analisis de datos en ventas
#Identificacion de tendencias y patrones en los numeros

import statistics
import csv

monthly_sales = {}
with open('monthly_sales.csv', mode = 'r')as file:
  reader = csv.DictReader(file)
  for linea in reader:
    month = linea['month']
    sales = int(linea['sales'])
    monthly_sales[month] = sales
    
sales = list(monthly_sales.values()) #Extrayendo los valores 
print(sales)

#Encontrar la media de los datos (Suma de todos los datos divididos entre el numero total)

mean_sales = statistics.mean(sales)
print(f"La media de ventas es: {mean_sales}")

#Encontra la mediana

median_sales = statistics.median(sales)
print(f"La mediana de ventas es: {median_sales}")

#Encontrar la moda

mode_sales = statistics.mode(sales)
print(f'La moda de ventas es: {mode_sales}')

#Encontrar la Desviacion Estandar

stdev_sales = statistics.stdev(sales)
print(f"La desviacion estandar de ventas es: {stdev_sales}")

#Encontrar la Variancia

variance_sales = statistics.variance(sales)
print(f"La varianza de ventas es; {variance_sales}")

#Encontrar el maximo y el minimo de ventas 

max_sales = max(sales)
min_sales = min(sales)

#Rango de ventas 

range_sales = max_sales - min_sales
print(f'El rango de ventas es: {range_sales}')