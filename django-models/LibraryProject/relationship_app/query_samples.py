import sys
import os
import django

# Ensure the project root is in the Python path
sys.path.append("/mnt/c/Users/Admin/Alx_DjangoLearnLab/django-models/LibraryProject")

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Define author and library names
author_name = "NoViolet Bulawayo"
library_name = "Nairobi Library"

# Ensure the author and library exist
author, _ = Author.objects.get_or_create(name=author_name)
library, _ = Library.objects.get_or_create(name=library_name)

# Create or get books
book1, _ = Book.objects.get_or_create(title="Glory", author=author)
book2, _ = Book.objects.get_or_create(title="We Need New Names", author=author)

# Add books to library
library.books.add(book1, book2)  

# Create or get librarian
librarian, _ = Librarian.objects.get_or_create(name="Maria Grace", library=library)

# Retrieve the librarian for the library using `.filter().first()` instead of `.get()`
librarian_for_library = Librarian.objects.filter(library=library).first()

# Display librarian details
if librarian_for_library:
    print(f"\nLibrarian for {library.name}: {librarian_for_library.name}")
else:
    print(f"\nNo librarian found for {library.name}.")

# Query and display all books by the specific author
print(f"\nBooks by {author_name}:")
books_by_author = Book.objects.filter(author=author)  
for book in books_by_author:
    print(f"- {book.title}")

# List all books in the library
print(f"\nBooks in {library.name}:")
books_in_library = library.books.all()
if books_in_library:
    for book in books_in_library:
        print(f"- {book.title}")
else:
    print("No books found in this library.")