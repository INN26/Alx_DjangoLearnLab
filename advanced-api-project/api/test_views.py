from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        """Set up initial test data"""
        self.book1 = Book.objects.create(title="Things Fall Apart", author="Chinua Achebe", publication_year=1958)
        self.book2 = Book.objects.create(title="Half of a Yellow Sun", author="Chimamanda Ngozi Adichie", publication_year=2006)
        self.valid_data = {"title": "Purple Hibiscus", "author": "Chimamanda Ngozi Adichie", "publication_year": 2003}
        self.invalid_data = {"title": "", "author": "Unknown", "publication_year": 2020}

    def test_get_book_list(self):
        """Test retrieving a list of books"""
        url = reverse('book-list')  # Ensure your URL name matches the router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """Test creating a new book"""
        url = reverse('book-list')
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_invalid_book(self):
        """Test creating a book with invalid data"""
        url = reverse('book-list')
        response = self.client.post(url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_book(self):
        """Test updating an existing book"""
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.put(url, {"title": "Things Fall Apart (Updated)", "author": "Chinua Achebe", "publication_year": 1958}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    def test_delete_book(self):
        """Test deleting a book"""
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        url = reverse('book-list') + "?author=Chinua Achebe"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        """Test searching books by title"""
        url = reverse('book-list') + "?search=Things Fall Apart"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """Test ordering books by publication year"""
        url = reverse('book-list') + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Things Fall Apart")  # 1958 comes before 2006