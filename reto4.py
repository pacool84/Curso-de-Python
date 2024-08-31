#Tendremos una consecionaria 
#Se pueden hacer compras y ventas de vehiculos
#Gestionar Vehiculos, Modelo, Precio, Disponibilidad, Color 

class Vehiculo:
    def __init__(self, modelo, precio, color):
        self.modelo = modelo
        self.precio = precio
        self.color = color
        self.available_car = True

    def vender(self):
        self.available_car = False
        print(f"El vehículo {self.modelo} ha sido vendido.")

    def comprar(self):
        self.available_car = True
        print(f"El vehículo {self.modelo} ha sido comprado y está disponible nuevamente.")


class Cliente:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def comprar_vehiculo(self, vehiculo, consecionaria):
        if vehiculo.available_car:
            consecionaria.vender_vehiculo(vehiculo)
            print(f"{self.name} ha comprado el vehículo {vehiculo.modelo} por ${vehiculo.precio}.")
        else:
            print(f"Lo siento, {self.name}, el vehículo {vehiculo.modelo} no está disponible.")

    def vender_vehiculo(self, vehiculo, consecionaria):
        consecionaria.comprar_vehiculo(vehiculo)
        print(f"{self.name} ha vendido el vehículo {vehiculo.modelo} por ${vehiculo.precio}.")


class Consecionaria:
    def __init__(self):
        self.cars_for_sell = []

    def register_a_car(self, car):
        self.cars_for_sell.append(car)
        print(f"Se ha registrado el vehículo {car.modelo} por un precio de ${car.precio}.")

    def show_pasarell_cars(self):
        print("Los vehículos disponibles son:")
        for car in self.cars_for_sell:
            if car.available_car:
                print(f"{car.modelo} ({car.color}) por un precio de ${car.precio}")

    def vender_vehiculo(self, vehiculo):
        if vehiculo in self.cars_for_sell and vehiculo.available_car:
            vehiculo.vender()
        else:
            print(f"El vehículo {vehiculo.modelo} no está disponible o no está registrado en la consecionaria.")

    def comprar_vehiculo(self, vehiculo):
        if vehiculo in self.cars_for_sell and not vehiculo.available_car:
            vehiculo.comprar()
        else:
            print(f"El vehículo {vehiculo.modelo} ya está disponible o no está registrado en la consecionaria.")


# Creamos los vehículos
vehiculo1 = Vehiculo("Mazda", 350000, "Rojo")
vehiculo2 = Vehiculo("Mini Cooper", 450000, "Azul")

# Creamos a los clientes
cliente1 = Cliente("Sebastian", "Chevy")

# Creamos la consecionaria
consecionaria = Consecionaria()

# Registramos los vehículos
consecionaria.register_a_car(vehiculo1)
consecionaria.register_a_car(vehiculo2)

# Mostrar los coches disponibles en la consecionaria
consecionaria.show_pasarell_cars()

# Cliente compra un vehículo
cliente1.comprar_vehiculo(vehiculo1, consecionaria)

# Mostrar los coches disponibles después de la compra
consecionaria.show_pasarell_cars()

# Cliente vende un vehículo
cliente1.vender_vehiculo(vehiculo1, consecionaria)

# Mostrar los coches disponibles después de la venta
consecionaria.show_pasarell_cars()