# 📚 Advanced API Project

This Django project demonstrates the use of Django REST Framework (DRF) with **generic views** to handle CRUD operations efficiently.

## 📌 Features
- Implements **ListView**, **DetailView**, **CreateView**, **UpdateView**, and **DeleteView** for the `Book` model.
- Uses Django REST Framework's generic views to simplify API development.
- Includes authentication-based permission handling.# 📚 Advanced API Project

## Book API - Filtering, Searching, and Ordering

### Filtering
You can filter books using:
- `?author=<author_name>`
- `?publication_year=<year>`

GET /api/books/?author=Chinua Achebe
### Searching
Search books by title or author:
### Ordering
Sort results using:
- `?ordering=title`
- `?ordering=publication_year`
- `?ordering=-publication_year` (Descending)
