retrieve = Book.objects.get("1984")
retrieve.__dict__
<!-- {'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949} -->