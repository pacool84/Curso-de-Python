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

class Bike(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"La bicicleta {self.brand} esta en marcha"
    else:
      return f"La bicicleta {self.brand} no esta disopnible"
  
  def stop_engine(self):
    if self.is_available:
      return f"La bicicleta {self.brand} se ha detenido"
    else:
      return f"La bicicleta {self.brand} no esta disponible"

class Truck(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"El motor del camion {self.brand} esta en marcha"
    else:
      return f"El camion {self.brand} no esta disponible"
    
  def stop_engine(self):
    if self.is_available:
      return f"El motor del camion {self.brand} se ha detenido"
    else:
      return f"El camion  {self.brand} no esta disponible"
    
class Customer():
  def __init__(self, name):
    self.name = name
    self.purchased_vehicles = []
    
  def buy_vehicle(self, vehicle: Vehicle): #Le pasamos la clase Padre / Superclase
    if vehicle.check_available():
      vehicle.sell() #Llamamos el metodo de la clase padre
      self.purchased_vehicles.append(vehicle)
    else:
      print(f"Lo siento el {vehicle.brand} no esta disponible")
      
  def inquire_vehicle(self, vehicle: Vehicle): #Funcion para preguntar por los vehiculos
    if vehicle.check_available():
      availability = "Disponible"
    else:
      availability = "No Disponible"
      
    print(f"El vehiculo {vehicle.brand} esta como {availability} y cuesta {vehicle.get_price()}")

class Dealership():
  def __init__(self):
    self.inventory = []
    self.customers = []
    
  def add_vehicles(self, vehicle: Vehicle):
    self.inventory.append(vehicle)
    print(f"El {vehicle.brand} ha sido añadido al inventario")
    
  def register_customers(self, customer: Customer):
    self.customers.append(customer)
    print(f"El cliente {customer.name} ha sido registrado")
    
  def show_available_vehicles(self):
    print("Vehiculos disponibles en la tienda:")
    for vehicle in self.inventory:
      if vehicle.check_available():
        print(f"El vehiculo {vehicle.brand} por {vehicle.get_price()}")
        
        
# Crear instancias de coches
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)

# Crear instancia de cliente
customer1 = Customer("Carlos")

# Crear instancia de concesionaria y registrar coches y clientes
dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(car2)
dealership.add_vehicles(car3)
dealership.register_customers(customer1)

# Mostrar coches disponibles
dealership.show_available_vehicles()

# Cliente consulta un coche
customer1.inquire_vehicle(car1)

# Cliente compra un coche
customer1.buy_vehicle(car1)

# Mostrar coches disponibles nuevamente
dealership.show_available_vehicles()

# Cliente intenta comprar un coche ya vendido
customer1.buy_vehicle(car1)