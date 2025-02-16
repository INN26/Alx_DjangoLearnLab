retrieve.title = "Nineteen Eighty-Four"
retrieve.save()
Book.objects.get(id = retrieve.id).title
<!-- 'Nineteen Eighty-Four' -->