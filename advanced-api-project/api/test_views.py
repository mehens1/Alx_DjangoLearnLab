class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Set up an authenticated user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')
        
        # Create initial data
        self.book = Book.objects.create(title='Django Unchained', author='Quentin Tarantino', publication_year=2012)
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})
    
    def test_create_book(self):
        """Test creating a new book"""
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': 'Author', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Django Unchained')
    
    def test_update_book(self):
        """Test updating an existing book"""
        data = {'title': 'Django Updated', 'author': 'Quentin Tarantino', 'publication_year': 2012}
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Django Updated')
    
    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

class BookFilteringTestCase(APITestCase):
    
    def setUp(self):
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2021)
        self.book3 = Book.objects.create(title='Book Three', author='Author A', publication_year=2022)
    
    def test_filter_by_author(self):
        """Test filtering by author"""
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_search_by_title(self):
        """Test searching by title"""
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_order_by_publication_year(self):
        """Test ordering by publication_year"""
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')
        self.assertEqual(response.data[2]['title'], 'Book Three')

class BookPermissionTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.book = Book.objects.create(title='Book Perm', author='Author C', publication_year=2021)
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})
    
    def test_anonymous_cannot_create_book(self):
        """Test that anonymous users cannot create a book"""
        url = reverse('book-list')
        data = {'title': 'Unauthorized', 'author': 'Author', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_authenticated_user_can_create_book(self):
        """Test that authenticated users can create a book"""
        self.client.login(username='testuser', password='password123')
        url = reverse('book-list')
        data = {'title': 'Authorized Book', 'author': 'Author', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
