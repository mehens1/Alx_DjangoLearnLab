from django.urls import path
from .views import BookListView
from .views import BookDetailView
from .views import BookCreateView
from .views import BookUpdateView
from .views import BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List all books and create a new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a specific book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]