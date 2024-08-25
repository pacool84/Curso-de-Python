# Recursividad
# La recursividad ocurre cuando una función se llama a sí misma para resolver un problema en partes más pequeñas.
# La clave es definir una condición base que detenga la recursión.


# Función para calcular el factorial de un número
# El factorial de n (denotado como n!) se define como n * (n-1) * (n-2) * ... * 1
# En términos recursivos: factorial(n) = n * factorial(n-1)
# Caso base: factorial(0) = 1


def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
  
print(factorial(5))

# Función para calcular el número en la serie de Fibonacci
# La serie de Fibonacci se define como:
# fib(n) = fib(n-1) + fib(n-2)
# Caso base: fib(0) = 0, fib(1) = 1


def fibonacci_sequence(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

fibonacci_number = 7  
print(fibonacci_sequence(fibonacci_number))
