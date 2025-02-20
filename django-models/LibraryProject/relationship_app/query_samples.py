import sys
import os
import django

# Ensure the project root is in the Python path
sys.path.append("/mnt/c/Users/Admin/Alx_DjangoLearnLab/django-models/LibraryProject")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
#create an Author querry
author1 = Author.objects.create(name="NoViolet Bulawayo")

#create a book querry
book1 = Book.objects.create(title="Glory", author=author1)
book2 = Book.objects.create(title="We Need New Names", author=author1)

# A library querry
Library1 = Library.objects.create(name = "Nairobi Library")
Library1.books.add(book1, book2)

#Librarian querry
Librarian1 = Librarian.objects.create(name="Maria Grace", library=Library1)

# Query all books by a specific author
author_books = Book.objects.filter(author=author1)
print("Books by Noviolet Bulawayo:")
for book in author_books:
    print(book.title)

# List all books in a library
library_name = "Nairobi Library"
library = Library.objects.filter(name=library_name).first()  

if library:  # Check if library exists
    books_in_library = library.books.all()  
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(book.title)
else:
    print(f"No library found with the name {library_name}")

 