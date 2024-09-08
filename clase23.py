'''
Métodos que Vienen por Defecto en Python
En Python, todas las clases heredan de la clase base object. Esto significa que todas las clases tienen ciertos métodos por defecto, algunos de los cuales pueden ser útiles para personalizar el comportamiento de tus clases.

Métodos por Defecto Más Comunes
__init__(self): Constructor de la clase. Es llamado cuando se crea una nueva instancia de la clase. Inicializa los atributos del objeto.
__str__(self): Devuelve una representación en cadena del objeto, utilizada por print() y str(). Este método es útil para proporcionar una representación legible del objeto.
__repr__(self): Devuelve una representación “oficial” del objeto, utilizada por repr(). Este método está diseñado para devolver una cadena que represente al objeto de manera que se pueda recrear.
Ejemplo de Métodos __str__ y __repr__
Vamos a crear una clase Person que sobrescriba los métodos __str__ y __repr__.


'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #El método __str__ devuelve una representación en cadena del objeto, útil para mensajes de salida amigables.
        return f"{self.name}, {self.age} años"

    def __repr__(self):#El método __repr__ devuelve una representación más detallada del objeto, útil para la depuración.
        return f"Person(name={self.name}, age={self.age})"

# Crear instancias de Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Uso de __str__
print(person1)  # Output: Alice, 30 años

# Uso de __repr__
print(repr(person1))  # Output: Person(name=Alice, age=30)