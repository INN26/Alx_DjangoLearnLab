from bookshelf.models import Book
book = Book.objects.create(title = "1984", author ="George Orwell", publication_year = 1949) 

<!-- Book:1984 -->

retrieve = Book.objects.get(title = "1984")
retrieve.__dict__
<!-- {'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949} -->

retrieve.title = "Nineteen Eighty-Four"
retrieve.save()
Book.objects.get(id = retrieve.id).title
<!-- retrieve'Nineteen Eighty-Four' -->

retrieve.delete()
Book.objects.all()
<!-- <QuerySet []> -->