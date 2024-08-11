#Listas de dimensiones y tuplas
#Se le conoce como matrices a aquellas listas que contienen mas listas

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
#Se debe de estar consiente que la matriz anterior va de 0 a 2 en filas y de 0 a 2 en columnas
#El numero "9" estaria posicionado en la fila = 2 y columna = 2 (2,2)

print(matrix)

#Con esta estructura accedemos a las filas
print(matrix[0])  # [1, 2, 3] -> Fila 0
print(matrix[1])  # [4, 5, 6] -> Fila 1
print(matrix[2])  # [7, 8, 9] -> Fila 2


#Agreguemos una dimension mas para acceder para un mejor entendimiento
#Queremos hacer el ejercicio con el numero 6 de la siguiente lista

new_matrix = [[[1,2],[3,4]], #Fila 0 de la primera dimension 
              [[5,6],[7,8]]] #Fila 1 de la primera dimension 

#En la fila 1, la lista [5, 6] representa la columna 0, y [7, 8] representa la columna 1.
#Dentro de [5, 6], 5 está en la columna 0 y 6 en la columna 1.
#Por lo tanto, la posición del número 6 es [1][0][1].


print(new_matrix[1][0][1])

#Las matrices tienen las mismas propiedas que las listas, se pueden agregar elementos, remorverlos
#etc, por lo que entonces decimos que son mutables







