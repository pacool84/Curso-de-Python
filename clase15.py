#Funciones en python
#Se utiliza la palabra reservada "def" y su sintaxis basica es la siguiente
def greet():
  print("Hola Mundo")

greet()

#Pasando parametros a una funcion
def new_greet(name):
  print("Hello", name)

new_greet("Paco") #Pasando parametros a una funcion 

#Pasando mas de un parametro
def hello_family(name1, name2):
  print(f"Hello {name1} y {name2}")

hello_family("Sebas", "Brenda")#Si no se llegara a pasar uno parametro que espera la funcion, enviaria un mensaje de error "missing 1 required positionalargument nombre_variable"

#Seteando paramaetros por default 

def without_parameters(name = "Sin nombre", last_name = "Sin apellido"):
  print(f"Hola {name} {last_name}")

without_parameters("Brenda", "Siurob")
without_parameters()#Al hacer este llamado de la funcion tomaria los valores default 

#Pasando parametros haciendo referencias

def sending_references(name = "Sin nombre", last_name = "Sin Apellido"):
  print(f"Hello {name} {last_name}")

sending_references(last_name="Rosales", name="Sebas")#Aqui mandamos referenciando los parametros pero sin seguir el orden de como estan en la funcion definidios


#Funciones para una calculadora

def add(a,b):
  return a + b

def substract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b

def calculator():
  while True:
    print("Seleccione una opcion")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Division")
    print("5.- Salir")
    
    option = int(input("Ingrese una opción: "))
    
    if option == 5:
      print("Saliendo de la calculadora....")
      break
    #Tambien se puede solucionar regresando un valor de falso "return False" en vez del break
      
    if option in [1,2,3,4]:
      num1 = float(input("Ingrese el primer numero: "))
      num2 = float(input("Ingrese el segundo numero: "))
      
      if option == 1:
        print("La suma es:", add(num1, num2))
      elif option == 2:
        print("La resta es:", substract(num1, num2))
      elif option == 3:
        print("La multiplicacion es:", multiply(num1, num2))
      elif option == 4:
        print("La division es:", divide(num1, num2))
    else:
      print("Opcion no valida, Intenta de nuevo...")
      
calculator()