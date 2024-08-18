#Bucles y Control de Iteraciones

numbers = [1,2,3,4,5,6]

""" for i in numbers:
  print("El valor de i es: ", i)
  if i == len(numbers) and i <= 100:
    numbers.append(i + 1)
    print(i) """

for i in numbers:
  print("El valor de i es: ", i)
  
#Iterar en un rango de datos 
#Range considera desde el 0 hasta n-1 de su rango especificado

for i in range(10): #Rango de 0 a 9
  print("El valor de i en el rango de 10 es: ",i)
  
#Podemos especificar el rango de inicio y termino para la funcion range()

for i in range(3,10):#Rango de 3 al 9
  print("Control de rango, inicio y termino: ", i)
  
#Agregando IF al un ciclo FOR 

alimentos = ["Manzana", "Uva","Carne", "Pera", "Tuna"]

for alimento in alimentos:
  if alimento == "Carne":
    print(f"Cuida tu alimentación, no consumas tanta {alimento}")
  else:
    print("Continua comiendo frutas y verduras: ", alimento)
    
#Iterar por medio de una "condicion" / WHILE

x = 0
while x <= 10:
  print(x)
  x += 1

#Utilizando la opcion de BREAK
#BREAK lo utilizamos para poder interrumpir una interacion o un ciclo // Interrumpimos el codigo

y = 0
while y <= 100:
  if y == 77:
    break
  print(y)
  y += 1
  
#Situaciones en donde no queremos terminar el codigo pero queremos saltar u omitir el paso que queremos evaluar
#Utilizando CONTINUE

new_numbers = [1,2,3,4,5,6]

for i in new_numbers:
  if i == 4:
    continue
  print(i) #No se imprime el numero 4