# La función SUPER
# La función super() en Python se utiliza para acceder a métodos y atributos de una superclase (o clase padre) desde una subclase (o clase hija).
# Esto es útil para extender las funcionalidades de la clase padre en la subclase sin tener que reescribir el código de la superclase.
# Es especialmente útil cuando queremos mantener y reutilizar el comportamiento de la superclase en la subclase.

# Repasando conceptos:
# - ATRIBUTOS: Son las características o propiedades de un objeto que se definen en una clase.
# - MÉTODOS: Son las acciones o comportamientos que un objeto puede realizar, definidos dentro de una clase.

class Person:
    def __init__(self, name, age):  # Constructor
        # Atributos que definen las características de una persona
        self.name = name  # Atributo 'name'
        self.age = age    # Atributo 'age'
    
    def greet(self):  # Método
        # Método que imprime un saludo usando el nombre del objeto Person
        print(f"Hello, I am {self.name}")
    
class Student(Person):  # Student hereda de Person
    def __init__(self, name, age, student_id):  
        # El constructor de la subclase Student necesita recibir los mismos atributos
        # de la superclase Person más los atributos adicionales de la subclase.
        
        # Llamada al constructor de la superclase para inicializar los atributos heredados (name y age)
        super().__init__(name, age)  
        
        # Atributo adicional propio de la subclase Student
        self.student_id = student_id  
    
    def greet_student(self):  
        # Llamada al método greet de la superclase Person usando super()
        super().greet()
        
        # Extensión del comportamiento del método greet para incluir el ID de estudiante
        print(f"Hello, my student ID is {self.student_id}")

# Creación de una instancia de la subclase Student
student1 = Student("Sebas", 9, "chevy15")

# El estudiante saluda usando el método greet_student de la subclase
student1.greet_student()