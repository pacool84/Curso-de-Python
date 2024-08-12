#Condicionales
age = input("Registra tu edad: ")
formated_age = int(age)

if formated_age > 18:
  print("Eres mayor de edad")

elif formated_age == 18:
  print("Apenas si pudiste entrar")

else:
  print("Eres menor de edad, NO puedes ingresar")

#Condicionales donde se evaluan dos parametros 
x = 15 
y = 20

if x > 10 and y < 25: #AMBAS condiciones deben de ser verdaderas para entrar en el print
  print("Ambas condiciones son verdaderas")


if x < 10 or y > 15: #Al menos una de las condicionales es verdadera
  print("Una de las dos es verdadera")

#Negar una condicional 
if not x < 10:
  print("Negando una condicional, X NO es menor que 10")


#IF ANIDADOS

is_member = True
age = 10

if is_member:
  if age >= 15:
    print("Tienes acceso, Eres miembro y mayor a 15 años")
  else:
    print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
  print("No eres miembro y NO TIENES ACCESO")