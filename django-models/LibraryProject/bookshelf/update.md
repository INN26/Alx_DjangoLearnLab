retrieve.title = "Nineteen Eighty-Four"
retrieve.save()
book = Book.objects.get(id = retrieve.id)
book.title
<!-- retrieve'Nineteen Eighty-Four' -->