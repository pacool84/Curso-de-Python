#El concepto de herencia en programación permite que una clase derive atributos y métodos de otra, facilitando la reutilización de código y la creación de estructuras jerárquicas lógicas. En este ejercicio, se aplica herencia para modelar una concesionaria que vende autos, bicicletas y camiones.


class Vehicle:
  def __init__(self, brand, model, price):
    #Las clases hijas van a heredar todos estos parametros de la superclase 
    self.brand = brand
    self.model = model
    self.price = price
    self.is_available = True

  def sell(self):
    if self.is_available:
      self.is_available = False
      print(f"El vehiculo {self.brand} ha sido vendido $$$ ")
    else:
      print(f"El vehiculo {self.brand} NO esta disponible ")
      
  def check_available(self):
    return self.is_available

  def get_price(self):
    return self.price
  
  def start_engine(self):
    raise NotImplementedError("Este metodo debe de ser implementado por la subclase")
  
  def stop_engine(self):
    raise NotImplementedError("Este metodo debe de ser implementado por la subclase ")
  
#Creacion de las clases hijas
#Estas clases HEREDARAN ATRIBUTOS Y METODOS de la Clase Padre / Superclase
#Sintaxis class child_class(parent_class):

class Car(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return print(f"El motor del coche {self.brand} esta en marcha")
    else:
      return print(f"El coche {self.brand} no esta disponible")
    
  def stop_engine(self):
    if self.is_available:
       return f"El motor del coche {self.brand} se ha detenido"
    else:
      return f"El coche {self.brand} no esta disponible"