# Funciones Lambda - Funciones Anónimas
# Las funciones lambda son útiles para operaciones simples que no necesitan un nombre.
# Son funciones pequeñas y de una sola línea que pueden tomar múltiples parámetros.
# La sintaxis general es: lambda argumentos: expresión

# Ejemplo de función lambda para sumar dos números
add = lambda a, b: a + b
print(add(10, 4))  # Salida: 14

# Ejemplo de función lambda para multiplicar dos números
multiply = lambda a, b: a * b
print(multiply(4, 2))  # Salida: 8

# Obtener el cuadrado de cada número en una lista
# Utilizamos la función map para aplicar una operación a cada elemento de la lista
# La función map toma una función y una iterable, y aplica la función a cada elemento del iterable.

numbers = range(11)  # Lista de números del 0 al 10
squared_numbers = list(map(lambda x: x**2, numbers))  # Aplicar la función lambda para calcular el cuadrado de cada número
print(squared_numbers)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filtrar elementos de una lista según una condición
# Utilizamos la función filter para seleccionar elementos que cumplen con una condición
# La función filter toma una función (que devuelve True o False) y un iterable, 
# y devuelve un iterable con los elementos para los cuales la función devuelve True.

# Obtener números pares de la lista
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filtrar números pares
print(even_numbers)  # Salida: [0, 2, 4, 6, 8, 10]
