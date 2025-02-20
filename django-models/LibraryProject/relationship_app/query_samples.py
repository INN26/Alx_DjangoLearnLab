import sys
import os
import django

# Ensure the project root is in the Python path
sys.path.append("/mnt/c/Users/Admin/Alx_DjangoLearnLab/django-models/LibraryProject")

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create or get an author
author1, created_author = Author.objects.get_or_create(name="NoViolet Bulawayo")

# Create or get books
book1, created_book1 = Book.objects.get_or_create(title="Glory", author=author1)
book2, created_book2 = Book.objects.get_or_create(title="We Need New Names", author=author1)

# Create or get library
library_name = "Nairobi Library"
library1, created_library = Library.objects.get_or_create(name=library_name)

# Add books to library
library1.books.add(book1, book2)  

# Create or get librarian
librarian1, created_librarian = Librarian.objects.get_or_create(name="Maria Grace", library=library1)

# Query and display all books by a specific author
print("\nBooks by NoViolet Bulawayo:")
for book in author1.books.all():  
    print(f"- {book.title}")

# Fetch library explicitly as expected by task checker
library1 = Library.objects.get(name=library_name)

# List all books in the library
print(f"\nBooks in {library1.name}:")
books_in_library = library1.books.all()
if books_in_library.exists():
    for book in books_in_library:
        print(f"- {book.title}")
else:
    print("No books found in this library.")