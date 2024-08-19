from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'app_name/book_list.html', {'books': books})

@permission_required('app_name.can_create', raise_exception=True)
def book_create(request):
    # Implementation for creating a book
    pass

@permission_required('app_name.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Implementation for editing a book
    pass

@permission_required('app_name.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Implementation for deleting a book
    pass
