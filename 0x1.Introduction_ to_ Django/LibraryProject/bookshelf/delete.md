# Deleting a Book Instance

```python
# Import the Book model
from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(id=<id_of_the_book_to_delete>)
book.delete()

# Verify deletion by checking the queryset
books = Book.objects.all()
print(books)