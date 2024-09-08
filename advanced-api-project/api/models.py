from django.db import models

class Author(models.Model):
    """Model representing an author."""
    # The name field stores the author's name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book."""
    # The title field stores the book title
    title = models.CharField(max_length=200)
    # The publication_year field stores the year the book was published
    publication_year = models.IntegerField()
    # The author field establishes a foreign key relationship to Author
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


