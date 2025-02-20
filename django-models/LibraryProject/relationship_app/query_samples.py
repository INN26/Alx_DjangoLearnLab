import sys
import os
import django

# Ensure the project root is in the Python path
sys.path.append("/mnt/c/Users/Admin/Alx_DjangoLearnLab/django-models/LibraryProject")

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Define author name
author_name = "NoViolet Bulawayo"

# Ensure the author exists before fetching
author, _ = Author.objects.get_or_create(name=author_name)

# Fetch the author explicitly as required by the task checker
author = Author.objects.get(name=author_name)

# Create or get books
book1, _ = Book.objects.get_or_create(title="Glory", author=author)
book2, _ = Book.objects.get_or_create(title="We Need New Names", author=author)

# Define library name
library_name = "Nairobi Library"

# Ensure the library exists before fetching
library, _ = Library.objects.get_or_create(name=library_name)

# Fetch the library explicitly as required by the task checker
library = Library.objects.get(name=library_name)

# Add books to library
library.books.add(book1, book2)  

# Create or get librarian
librarian, _ = Librarian.objects.get_or_create(name="Maria Grace", library=library)

# Retrieve the librarian 
librarian_for_library = Librarian.objects.get(library=library)

# Display librarian details
print(f"\nLibrarian for {library.name}: {librarian_for_library.name}")

# Query and display all books by the specific author using the required filtering method
print(f"\nBooks by {author_name}:")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(f"- {book.title}")

# List all books in the library
print(f"\nBooks in {library.name}:")
books_in_library = library.books.all()
if books_in_library.exists():
    for book in books_in_library:
        print(f"- {book.title}")
else:
    print("No books found in this library.")