#Existen parametros que se pueden agregar a la funcion print para aumentar su funcionalidad 

#Parametro sep, se utiliza para decirle a print como separar los strings 

print("hola","mi","amigo", sep=", ")

#El parámetro end cambia lo que se imprime al final de la llamada a print.
#  En lugar de imprimir cada mensaje en una nueva línea, end="" asegura que “Nunca” y “pares” se impriman en la misma línea, resultando en “Nunca pares”. 
# Por defecto, end es un salto de línea ("\n"), lo que hace que cada llamada a print comience en una nueva línea.

print("Nunca", end=" ")
print("pares de aprender")

#Impresion de variables 

frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#Uso de formato con f-strings
name = "Francisco"
last_name = "López"
print(f"Nombre: {name}, Apellido: {last_name}")
print(f"Nombre completo: {name} {last_name}")

#Uso de formato con format
#El método format es otra forma de insertar valores en cadenas de texto. 
#Usando {} como marcadores de posición, puedes pasar los valores que quieres insertar como argumentos de format. 
#En este ejemplo, se imprimirá “Frase: Nunca pares de aprender, Autor: Platzi”. 
# Es una forma flexible y poderosa de formatear cadenas, aunque las f-strings son más concisas.

new_name = "Jesus"
new_last = "Rodriguez"

print("El nombre completo es {} {}".format(new_name, new_last))

#Impresión con formato específico
#Puedes controlar el formato de los números al imprimir. 
#En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales. 
#Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales. 
# Esto es especialmente útil cuando trabajas con datos numéricos y necesitas un formato específico.

number = 3.14159
print("Valor: {:.2f}".format(number))
