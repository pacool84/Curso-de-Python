# Funciones en Python
# Se utiliza la palabra reservada "def" para definir una función.
# La sintaxis básica es la siguiente:

def greet():
    """Imprime un saludo básico."""
    print("Hola Mundo")

greet()

# Pasando parámetros a una función
def new_greet(name):
    """Imprime un saludo personalizado con el nombre proporcionado."""
    print("Hello", name)

new_greet("Paco")  # Llama a la función con el parámetro "Paco"

# Pasando más de un parámetro
def hello_family(name1, name2):
    """Imprime un saludo personalizado para dos nombres."""
    print(f"Hello {name1} y {name2}")

hello_family("Sebas", "Brenda")  # Llama a la función con dos parámetros

# Seteando parámetros por defecto
def without_parameters(name="Sin nombre", last_name="Sin apellido"):
    """Imprime un saludo con nombre y apellido, usando valores por defecto si no se proporcionan."""
    print(f"Hola {name} {last_name}")

without_parameters("Brenda", "Siurob")  # Usa valores proporcionados
without_parameters()  # Usa los valores por defecto

# Pasando parámetros haciendo referencia
def sending_references(name="Sin nombre", last_name="Sin Apellido"):
    """Imprime un saludo con nombre y apellido, permitiendo especificar el orden de los parámetros."""
    print(f"Hello {name} {last_name}")

sending_references(last_name="Rosales", name="Sebas")  # Llama a la función usando nombres de parámetros

# Funciones para una calculadora
def add(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def substract(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def multiply(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b

def divide(a, b):
    """Devuelve la división de dos números. Lanza un error si se intenta dividir por cero."""
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculator():
    """Calculadora simple que permite al usuario seleccionar una operación y realizar cálculos."""
    while True:
        print("\nSeleccione una opción:")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Salir")
        
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción no válida, por favor ingrese un número entero.")
            continue
        
        if option == 5:
            print("Saliendo de la calculadora...")
            break
        
        if option in [1, 2, 3, 4]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Entrada no válida, por favor ingrese un número.")
                continue
            
            if option == 1:
                print("La suma es:", add(num1, num2))
            elif option == 2:
                print("La resta es:", substract(num1, num2))
            elif option == 3:
                print("La multiplicación es:", multiply(num1, num2))
            elif option == 4:
                result = divide(num1, num2)
                if isinstance(result, str):  # Verifica si el resultado es un mensaje de error
                    print(result)
                else:
                    print("La división es:", result)
        else:
            print("Opción no válida, intenta de nuevo...")

calculator()
