#Ejercicio Gestion de Biblioteca
#Tendras las clases Libros, Persona, Biblioteca 

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True
  
  def borrow(self):
    if self.available == True:
      self.available = False
      print(f"El libro {self.title} se ha prestado")
    else:
      print(f"El libro {self.title} no esta disponible")
      
  def return_book(self):
    self.available = True
    print(f"El libro {self.title} ha sido devuelto")
    
class User:
  def  __init__(self, name, user_id):
    self.name = name
    self.user_id = user_id
    self.borrowed_books = []
    
  def borrow_book(self, book):
    if book.available:
      book.borrow()
      self.borrowed_books.append(book)
    else:
      print(f"El libro {book.title} no esta disponible")
  
  def return_book(self, book):
    if book in self.borrow_book:
      book.return_book()
      self.borrowed_books.remove(book)
    else:
      print(f"El libro {book.title} no esta en la lista de prestados")
      
class Library:
  def __init__(self):
    self.books = []
    self.users = []
    
  def add_book(self, book):
    self.books.append(book)
    print(f"El libro {book.title} ha sido agregado")
    
  def register_user(self, user):
    self.users.append(user)
    print(f"El usuario {user.name} ha sido agregado ")
    
  def show_available_books(self):
     print(f"Los libros disponibles son:")
     for book in self.add_book:
       if book.available:
         print(f"{book.title} por {book.author}")