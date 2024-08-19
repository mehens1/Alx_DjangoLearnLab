from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .models import Book
from .forms import ExampleForm
from .forms import BookForm

@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'app_name/book_list.html', {'books': books})

@permission_required('app_name.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

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

def book_search(request):
    query = request.GET.get('q', '')
    # Parameterized query to prevent SQL injection
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})