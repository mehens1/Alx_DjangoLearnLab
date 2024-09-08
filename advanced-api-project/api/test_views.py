from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create an author
        self.author = Author.objects.create(name='J.K. Rowling')
        # Create a book
        self.book = Book.objects.create(
            title='Harry Potter and the Philosopher\'s Stone',
            publication_year=1997,
            author=self.author
        )
        self.book_url = reverse('book-list')  # URL for list/create
        self.book_detail_url = reverse('book-detail', args=[self.book.id])  # URL for detail/update/delete

    def test_create_book(self):
        data = {
            'title': 'Harry Potter and the Chamber of Secrets',
            'publication_year': 1998,
            'author': self.author.id
        }
        response = self.client.post(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'Harry Potter and the Chamber of Secrets')

    def test_update_book(self):
        data = {'title': 'Harry Potter and the Philosopher\'s Stone (Updated)'}
        response = self.client.patch(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Harry Potter and the Philosopher\'s Stone (Updated)')

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_authentication(self):
        response = self.client.get(self.book_url)  # without authentication
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.book_url)  # with authentication
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filtering(self):
        response = self.client.get(self.book_url, {'title': 'Harry Potter and the Philosopher\'s Stone'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_searching(self):
        response = self.client.get(self.book_url, {'search': 'Chamber'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_ordering(self):
        response = self.client.get(self.book_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # should be ordered by publication_year
