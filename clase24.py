#Manejo de archivos .txt

#Leer un archivo linea por linea
with open('cuento.txt', 'r') as file:
  for cada_linea in file:
   print(cada_linea.strip())#utilizamos el metodo strip para poder quitar espacios innecesarios
      
#Leer todas las lineas en una lista

with open('cuento.txt', 'r') as file:
  lines = file.readlines()
  print(lines)
  
with open('cuento.txt', 'a') as file: #La letra "a" hace referencia al termino append, añade al final
  file.write("\n\nIn colaboration with Pacool84")

##Sobre escribir informacion en archivos, usarlo con precaucion 

with open ('cuento.txt', 'w') as file: #La leta "w" hace referencia al modo 
  file.write("Hemos borrado el archivo")