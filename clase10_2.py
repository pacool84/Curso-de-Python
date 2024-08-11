#TUPLAS, Son inmutables por lo que significa que no las podemos modificar
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))

#Accediendo a la informacion de la tuplas
print(numbers[0])
print(numbers[0:2])

#La alternativa para poder modificar las tuplas es guardarlas sin los parantesis 

new_numbers = 1,2,3,4,5
print(numbers)
print(type(numbers)) #Se sigue manteniendo como tipo Tupla

new_numbers[0] = "uno"
print(new_numbers)


#Tuplas en Python
#Tuplas: Las tuplas son una colección ordenada e inmutable de elementos en Python. Una vez creadas, no pueden ser modificadas (no se pueden agregar, eliminar o cambiar sus elementos).
#Ejemplo de Tupla

numbers = (1, 2, 3, 4, 5)
print(numbers)           # (1, 2, 3, 4, 5)
print(type(numbers))     # <class 'tuple'>

#Acceso a Elementos
#Puedes acceder a los elementos de una tupla de manera similar a una lista, utilizando índices.

print(numbers[0])    # 1 -> Accede al primer elemento
print(numbers[0:2])  # (1, 2) -> Accede a un rango de elementos (del índice 0 al 1)

#Inmutabilidad de las Tuplas
#Inmutable: Significa que una vez que se crea una tupla, sus elementos no se pueden cambiar.
#Intentar modificar un elemento de una tupla resultará en un error:

numbers[0] = 10  # Esto generará un TypeError

#Alternativas para Modificar Tuplas
#Aunque las tuplas son inmutables, hay maneras indirectas de "modificarlas":

#Convertir la Tupla en Lista:

#Convierte la tupla en una lista, realiza los cambios y luego vuelve a convertirla en tupla.

numbers_list = list(numbers)  # Convierte la tupla en lista
numbers_list[0] = 10          # Modifica el primer elemento
numbers = tuple(numbers_list) # Vuelve a convertir la lista en tupla
print(numbers)                # (10, 2, 3, 4, 5)

#Concatenar Tuplas:

#Puedes crear una nueva tupla concatenando partes de la tupla original con nuevos elementos.

numbers = (1, 2, 3, 4, 5)
new_numbers = (10,) + numbers[1:]  # Crea una nueva tupla con el primer elemento modificado
print(new_numbers)                 # (10, 2, 3, 4, 5)
#Tuplas Sin Paréntesis
#Puedes crear tuplas sin usar paréntesis explícitamente:

new_numbers = 1, 2, 3, 4, 5
print(new_numbers)          # (1, 2, 3, 4, 5)
print(type(new_numbers))    # <class 'tuple'>
#Nota: Aunque no uses paréntesis, Python sigue reconociendo la variable new_numbers como una tupla.

#Error de Modificación:
#Intentar modificar una tupla, sin importar si se define con o sin paréntesis, resultará en un error.

new_numbers[0] = "uno"  # Esto generará un TypeError
#Operaciones Comunes con Tuplas
#Desempaquetado: Puedes asignar los elementos de una tupla a variables individuales.

a, b, c, d, e = numbers
print(a)  # 1
print(b)  # 2

#Uso en Funciones: Las tuplas son útiles cuando necesitas asegurarte de que una colección de elementos no se modificará, como cuando retornas múltiples valores desde una función.

#Resumen
#Las tuplas son inmutables, lo que las hace ideales para almacenar datos que no deben cambiar.
#Para modificar una tupla, debes usar métodos indirectos, como convertirla a una lista o concatenar nuevas tuplas.
#Python permite la creación de tuplas sin paréntesis, pero estas siguen siendo inmutables.