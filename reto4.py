#Tendremos una consecionaria 
#Se pueden hacer compras y ventas de vehiculos
#Gestionar Vehiculos, Modelo, Precio, Disponibilidad, Color 

class Vehiculo:
  def __init__(self, modelo, precio):
    self.modelo = modelo
    self.precio = precio
    self.available_car = True
    

class Cliente:
  def __init__(self, name, user_id):
    self.name = name
    self.user_id = user_id
    

class Consecionaria:
  def __init__(self):
    self.cars_for_sell = []
    
  def register_a_car(self, car):
    self.cars_for_sell.append(car)
    print(f"Se ha registrado el vehiculo {car.modelo} por un precio de ${car.precio}")

##Creamos los vehiculos
vehiculo1 = Vehiculo("Mazda", 350000)

#Creamos a los clientes
cliente1 = Cliente("Sebastian", "Chevy")

#Creamos la consecionaria
consecionaria = Consecionaria()

#Registramos un vehiculo
consecionaria.register_a_car(vehiculo1)