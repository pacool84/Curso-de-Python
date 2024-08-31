# Ejercicio: Gestión de Biblioteca
# Este ejercicio modela una biblioteca que gestiona libros y usuarios.
# Contiene tres clases principales: Book, User y Library.

class Book:
    def __init__(self, title, author):
        """
        Inicializa un nuevo libro con un título, autor y estado de disponibilidad.
        :param title: Título del libro.
        :param author: Autor del libro.
        """
        self.title = title
        self.author = author
        self.available = True  # Estado del libro, True si está disponible.

    def borrow(self):
        """
        Marca el libro como prestado si está disponible.
        """
        if self.available:
            self.available = False
            print(f"El libro '{self.title}' se ha prestado.")
        else:
            print(f"El libro '{self.title}' no está disponible.")

    def return_book(self):
        """
        Marca el libro como disponible.
        """
        self.available = True
        print(f"El libro '{self.title}' ha sido devuelto.")

class User:
    def __init__(self, name, user_id):
        """
        Inicializa un nuevo usuario con un nombre, ID de usuario y una lista de libros prestados.
        :param name: Nombre del usuario.
        :param user_id: Identificación única del usuario.
        """
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []  # Lista de libros prestados por el usuario.

    def borrow_book(self, book):
        """
        Permite que el usuario tome prestado un libro si está disponible.
        :param book: Instancia de la clase Book a prestar.
        """
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro '{book.title}' no está disponible.")

    def return_book(self, book):
        """
        Permite que el usuario devuelva un libro previamente prestado.
        :param book: Instancia de la clase Book a devolver.
        """
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro '{book.title}' no está en la lista de prestados.")

class Library:
    def __init__(self):
        """
        Inicializa una nueva biblioteca con listas vacías de libros y usuarios.
        """
        self.books = []  # Lista de libros en la biblioteca.
        self.users = []  # Lista de usuarios registrados en la biblioteca.

    def add_book(self, book):
        """
        Agrega un nuevo libro a la biblioteca.
        :param book: Instancia de la clase Book a agregar.
        """
        self.books.append(book)
        print(f"El libro '{book.title}' ha sido agregado.")

    def register_user(self, user):
        """
        Registra un nuevo usuario en la biblioteca.
        :param user: Instancia de la clase User a registrar.
        """
        self.users.append(user)
        print(f"El usuario '{user.name}' ha sido registrado.")

    def show_available_books(self):
        """
        Muestra todos los libros disponibles en la biblioteca.
        """
        print("Libros disponibles en la biblioteca:")
        for book in self.books:
            if book.available:
                print(f"'{book.title}' por {book.author}")

# Creación de objetos y operaciones

# Crear instancias de libros
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")

# Crear una instancia de usuario
user1 = User("Francisco Lopez", "pacool84")

# Crear una instancia de la biblioteca
library = Library()

# Agregar libros a la biblioteca
library.add_book(book1)
library.add_book(book2)

# Registrar un usuario en la biblioteca
library.register_user(user1)

# Mostrar libros disponibles
library.show_available_books()

# El usuario toma prestado un libro
user1.borrow_book(book1)

# Mostrar libros disponibles después del préstamo
library.show_available_books()

# El usuario devuelve el libro
user1.return_book(book1)

# Mostrar libros disponibles después de la devolución
library.show_available_books()
