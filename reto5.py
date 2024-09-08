#Imprime el numero de lineas totales que tiene el archivo cuento.txt

with open('cuento.txt', 'r') as file:
  total_lines = file.readlines()
  print(f'El total de lineas en este archivo es de: {len(total_lines)} lineas')