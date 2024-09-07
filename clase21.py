# Los cuatro pilares de la POO son:
# Herencia, Abstracción, Encapsulamiento y Polimorfismo

class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulación: los atributos 'brand', 'model', 'price', y 'is_available' están encapsulados dentro de la clase.
        # Esto significa que no pueden ser accedidos directamente desde fuera de la clase sin utilizar métodos específicos.
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        # Método para vender un vehículo. Cambia el estado de disponibilidad del vehículo.
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido")
        else:
            print(f"El vehículo {self.brand} no está disponible")
    
    # Abstracción: estos métodos exponen solo lo necesario, ocultando la lógica interna de cómo se maneja la disponibilidad y el precio.
    def check_available(self):
        # Método que verifica si el vehículo está disponible para la venta.
        return self.is_available
    
    def get_price(self):
        # Método que retorna el precio del vehículo.
        return self.price
    
    def start_engine(self):
        # Método abstracto que obliga a las subclases a proporcionar una implementación específica.
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def stop_engine(self):
        # Método abstracto que obliga a las subclases a proporcionar una implementación específica.
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Herencia: la clase Car hereda de Vehicle, lo que significa que adopta todos sus atributos y métodos.
class Car(Vehicle):
    # Polimorfismo: estos métodos sobrescriben (overriding) los métodos abstractos de la clase padre para proporcionar una funcionalidad específica para los coches.
    def start_engine(self):
        # Implementación específica del método para arrancar el motor de un coche.
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"
    
    def stop_engine(self):
        # Implementación específica del método para detener el motor de un coche.
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"

# Herencia: la clase Bike hereda de Vehicle, lo que significa que adopta todos sus atributos y métodos.
class Bike(Vehicle):
    # Polimorfismo: similar a la clase Car, Bike sobrescribe los métodos abstractos de Vehicle para adaptarse a las características de una bicicleta.
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"

# Herencia: la clase Truck hereda de Vehicle, lo que significa que adopta todos sus atributos y métodos.
class Truck(Vehicle):
    # Polimorfismo: Truck sobrescribe los métodos abstractos de Vehicle para adaptarse a las características de un camión.
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"

# La clase Customer modela un cliente que puede comprar vehículos.
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        # Método para que el cliente compre un vehículo. Se verifica si el vehículo está disponible antes de proceder con la compra.
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        # Método para que el cliente consulte la disponibilidad y precio de un vehículo.
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El {vehicle.brand} está {availability} y cuesta {vehicle.get_price()}")

# La clase Dealership modela una concesionaria que maneja un inventario de vehículos y clientes.
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        # Método para añadir vehículos al inventario de la concesionaria.
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        # Método para registrar un nuevo cliente en la concesionaria.
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        # Método para mostrar todos los vehículos disponibles en el inventario.
        print("Vehículos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

# Crear instancias de vehículos
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

# Crear instancia de cliente
customer1 = Customer("Carlos")

# Crear instancia de concesionaria y registrar vehículos y clientes
dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Mostrar vehículos disponibles
dealership.show_available_vehicle()

# Cliente consulta un vehículo
customer1.inquire_vehicle(car1)

# Cliente compra un vehículo
customer1.buy_vehicle(car1)

# Mostrar vehículos disponibles nuevamente
dealership.show_available_vehicle()