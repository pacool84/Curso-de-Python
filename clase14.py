#Generadores e Iteradores
#Son muy utiles al estar trabajando con COLECCIONES

#Iteradores sin utilizar indices
#Crear una lista

my_list = [1,2,3,4]

my_iter = iter(my_list) #Obtener el iterador

print(next(my_iter)) #NEXT nos ayuda a poder ir viendo cuales son los valores que se van guardando en memoria
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter)) En caso de que excedamos la cantidad de indices dentro de la lista, nos enviara un mensaje de STOPITERATION

#Iteradores sobre STRINGS

text = "Hola Mundo"
iter_text = iter(text)
for caracter in iter_text:
  print(caracter)
  
#Iteradores para numeros impares 

limit = 10

odd_itter = iter(range(1,limit + 1,2)) #Para la funcion range se interpreta como que empieza en "1" y va hasta "limit + 1" y va de dos en dos
for numero in odd_itter:
  print(numero)
  
#Generadores, una funcion que produce una secuencia de numeros en los cuales podemos iterar 

#YIELD, es como utilizar return en otros lenguajes

def my_generator():
  yield 1
  yield 2
  yield 100
  
for value in my_generator():
  print(value)

#Creacion de la serie de fibonacci
# 0 1 1 2 3 5 8 13 21.....

def fibonacci(limit):
  a , b = 0, 1
  while a < limit :
    yield a
    a, b = b, a + b
    
for numero in fibonacci(1000):
  print(f"La serie de fibonacci va en: {numero}")