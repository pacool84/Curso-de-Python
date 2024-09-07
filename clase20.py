# El concepto de herencia en programación permite que una clase derive atributos y métodos de otra, 
# facilitando la reutilización de código y la creación de estructuras jerárquicas lógicas.
# En este ejercicio, se aplica herencia para modelar una concesionaria que vende autos, bicicletas y camiones.

class Vehicle:
    def __init__(self, brand, model, price):
        # Los atributos 'brand', 'model', y 'price' serán compartidos por todas las clases que hereden de Vehicle.
        # 'is_available' es un atributo que indica la disponibilidad del vehículo para la venta.
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        # Método para marcar un vehículo como vendido.
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido $$$ ")
        else:
            print(f"El vehículo {self.brand} NO está disponible")

    def check_available(self):
        # Método que retorna la disponibilidad del vehículo.
        return self.is_available

    def get_price(self):
        # Método que retorna el precio del vehículo.
        return self.price

    def start_engine(self):
        # Método abstracto que debe ser implementado por las subclases, ya que la acción de arrancar
        # el motor depende del tipo de vehículo.
        raise NotImplementedError("Este método debe de ser implementado por la subclase")

    def stop_engine(self):
        # Método abstracto que debe ser implementado por las subclases, ya que la acción de detener
        # el motor depende del tipo de vehículo.
        raise NotImplementedError("Este método debe de ser implementado por la subclase")


# Creación de las clases hijas.
# Estas clases HEREDARÁN ATRIBUTOS Y MÉTODOS de la Clase Padre / Superclase 'Vehicle'.
# Sintaxis: class child_class(parent_class):

class Car(Vehicle):
    def start_engine(self):
        # Implementación específica para los coches. Se revisa si el coche está disponible antes de encender el motor.
        if not self.is_available:
            return print(f"El motor del coche {self.brand} está en marcha")
        else:
            return print(f"El coche {self.brand} no está disponible")

    def stop_engine(self):
        # Implementación específica para los coches. Se revisa si el coche está disponible antes de apagar el motor.
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"


class Bike(Vehicle):
    def start_engine(self):
        # Las bicicletas generalmente no tienen motor, pero este método podría representar encender luces
        # u otra característica específica.
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"

    def stop_engine(self):
        # Método que simula detener alguna función de la bicicleta.
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"


class Truck(Vehicle):
    def start_engine(self):
        # Implementación específica para los camiones. Se revisa si el camión está disponible antes de encender el motor.
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"

    def stop_engine(self):
        # Implementación específica para los camiones. Se revisa si el camión está disponible antes de apagar el motor.
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"


class Customer():
    def __init__(self, name):
        # La clase Customer modela un cliente que puede comprar vehículos.
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        # Método para que el cliente compre un vehículo.
        # Verificamos si el vehículo está disponible antes de proceder con la compra.
        if vehicle.check_available():
            vehicle.sell()  # Se llama al método 'sell' de la clase padre para marcar el vehículo como vendido.
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, el {vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        # Método para que el cliente consulte la disponibilidad y precio de un vehículo.
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No Disponible"

        print(f"El vehículo {vehicle.brand} está como {availability} y cuesta {vehicle.get_price()}")


class Dealership():
    def __init__(self):
        # La clase Dealership modela una concesionaria que maneja un inventario de vehículos y clientes.
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        # Método para añadir vehículos al inventario de la concesionaria.
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        # Método para registrar un nuevo cliente en la concesionaria.
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")

    def show_available_vehicles(self):
        # Método para mostrar todos los vehículos disponibles en el inventario.
        print("Vehículos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"El vehículo {vehicle.brand} por {vehicle.get_price()}")


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