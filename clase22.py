#Funcion SUPER
#Nos permite acceder y llamar a metodos de la SUPER CLASE pero desde la SUBCLASE,facilita la extension de las FUNCIONALIDADES
#Repasando clases anteriores, ATRIBUTOS .- Son las caracteristicas que tiene la clase, Metodos .- Son acciones o cosas que sabe hacer la clase

class Person:
  def __init__(self, name, age):#Constructor
    self.name = name #Atributo
    self.age = age #Atributo
    
  def greet(self): #Metodo
    print(f"Hello I am {self.name}")
    
class Student(Person):
  def __init__(self, name, age, student_id):#Debemos de pedir los mismos atributos que se heredan de la SUPER CLASE mas los que quiera agregar en la subclase
   super().__init__(name, age) #Llamando al constructor de la SUPER CLASE y sus atributos
   self.student_id = student_id #Este atributo solo es de la SUBCLASE
  
  def greet_student(self):
    super().greet() #Llamamos al metodo greet de la SUPERCLASE
    print(f"Hello, my student ID is {self.student_id}")
    
#Creando las instancias de estudiantes pero haciendolo desde la SUBCLASE
student1 = Student("Sebas", 9, "chevy15")

#Estudiante Saluda
student1.greet_student()

