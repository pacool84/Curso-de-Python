# La Programación Orientada a Objetos (POO) es un paradigma de la programación 
# que organiza el software en objetos. Estos objetos son instancias de clases.

# Las clases son plantillas o moldes que definen la estructura y el comportamiento 
# (atributos y métodos) que los objetos de esa clase tendrán.

# Los objetos son instancias particulares de una clase. Es decir, son ejemplares 
# concretos que tienen valores específicos en sus atributos.

# Generando una clase

class Person:
    def __init__(self, name, age): 
        # El método __init__ es el constructor de la clase. Se ejecuta automáticamente 
        # al crear una nueva instancia (objeto) de la clase. Aquí se definen los 
        # atributos de la clase (name y age).
        self.name = name  # Atributo 'name' se asigna al valor pasado como argumento.
        self.age = age    # Atributo 'age' se asigna al valor pasado como argumento.
  
    def greet(self):
        # Este es un método de la clase. Los métodos definen el comportamiento de los objetos.
        # En este caso, greet es un método que imprime un saludo con el nombre y la edad del objeto.
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años de edad")
    
# Creando instancias (objetos) de la clase Person
person1 = Person("Sebas", 30)
person2 = Person("Bren", 25)

# Llamando a métodos de los objetos
person1.greet()  # Salida: Hola, mi nombre es Sebas y tengo 30 años de edad
person2.greet()  # Salida: Hola, mi nombre es Bren y tengo 25 años de edad

# Ejemplo para el manejo de una cuenta bancaria

class BankAccount:
    def __init__(self, account_holder, balance):
        # Constructor de la clase BankAccount. Define los atributos account_holder, balance e is_active.
        self.account_holder = account_holder  # Atributo 'account_holder' es el titular de la cuenta.
        self.balance = balance  # Atributo 'balance' es el saldo inicial de la cuenta.
        self.is_active = True  # Atributo 'is_active' indica si la cuenta está activa o no.
  
    def deposit(self, amount):
        # Método para depositar dinero en la cuenta.
        if self.is_active:  # Verifica si la cuenta está activa.
            self.balance += amount  # Incrementa el saldo de la cuenta.
            print(f"Se ha depositado ${amount}. Saldo actual es ${self.balance}")
        else:
            print("Usted no tiene una cuenta bancaria activa")
  
    def withdraw(self, amount):
        # Método para retirar dinero de la cuenta.
        if self.is_active:  # Verifica si la cuenta está activa.
            if amount <= self.balance:  # Asegura que haya suficiente saldo para el retiro.
                self.balance -= amount  # Decrementa el saldo de la cuenta.
                print(f"Se ha retirado ${amount}. Su nuevo balance es ${self.balance}")
            else:
                print("Fondos insuficientes")  # Si el saldo no es suficiente, muestra un mensaje.
        else:
            print("Usted no tiene una cuenta bancaria activa")
  
    def deactivate_account(self):
        # Método para desactivar la cuenta.
        self.is_active = False  # Cambia el estado de la cuenta a inactiva.
        print("La cuenta ha sido desactivada :( ")
  
    def activate_account(self):
        # Método para activar la cuenta.
        self.is_active = True  # Cambia el estado de la cuenta a activa.
        print("La cuenta ha sido activada :) ")

# Creación de objetos de la clase BankAccount
account1 = BankAccount("Brenda", 300000)
account2 = BankAccount("Sebas", 500)

# Aplicando los métodos de la clase
account1.deposit(300)  # Deposita dinero en account1
account2.deposit(500)  # Deposita dinero en account2

account1.withdraw(300)  # Retira dinero de account1
account2.withdraw(500)  # Retira dinero de account2

account1.deactivate_account()  # Desactiva la cuenta account1
account2.deactivate_account()  # Desactiva la cuenta account2
account1.deposit(4000)  # Intenta depositar dinero en una cuenta desactivada

account1.activate_account()  # Activa la cuenta account1
account2.activate_account()  # Activa la cuenta account2
