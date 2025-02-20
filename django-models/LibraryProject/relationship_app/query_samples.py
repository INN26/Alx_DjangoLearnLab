import sys
import os
import django

# Ensure the project root is in the Python path
sys.path.append("/mnt/c/Users/Admin/Alx_DjangoLearnLab/django-models/LibraryProject")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create or get an author
author1, _ = Author.objects.get_or_create(name="NoViolet Bulawayo")

# Create or get books
book1, _ = Book.objects.get_or_create(title="Glory", author=author1)
book2, _ = Book.objects.get_or_create(title="We Need New Names", author=author1)

# Create or get library
Library1, _ = Library.objects.get_or_create(name="Nairobi Library")
Library1.books.add(book1, book2)  # Ensure books are linked

# Create or get librarian
Librarian1, _ = Librarian.objects.get_or_create(name="Maria Grace", library=Library1)

# Query all books by a specific author
author_books = Book.objects.filter(author=author1)
print("Books by Noviolet Bulawayo:")
for book in author_books:
    print(book.title)

# List all books in a library
library_name = "Nairobi Library"
library, _ = Library.objects.get_or_create(name=library_name)
books_in_library = library.books.all()

print(f"Books in {library_name}:")
if books_in_library.exists():
    for book in books_in_library:
        print(book.title)
else:
    print("No books found in this library.")

# Retrieve the librarian for the library
librarian = library.librarian
if librarian:
    print(f"\nLibrarian of {library_name}: {librarian.name}")
else:
    print("\nNo librarian assigned to this library.")
 