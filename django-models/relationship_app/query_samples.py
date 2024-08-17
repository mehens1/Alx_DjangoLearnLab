import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    try:
        librarian = Librarian.objects.get(library=library)
        print(librarian.name)
    except Librarian.DoesNotExist:
        print("No librarian assigned to this library.")

# Example usage:
if __name__ == "__main__":
    print("Books by Author 'John Doe':")
    books_by_author('John Doe')
    
    print("\nBooks in Library 'Main Library':")
    books_in_library('Main Library')
    
    print("\nLibrarian for Library 'Main Library':")
    librarian_for_library('Main Library')
