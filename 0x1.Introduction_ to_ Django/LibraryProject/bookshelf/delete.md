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

# Output of the delete operation
(1, {'bookshelf.Book': 1})

# Output of the verification (should be an empty queryset if deletion was successful)
<QuerySet []>