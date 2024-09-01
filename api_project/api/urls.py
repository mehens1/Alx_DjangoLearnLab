from django.urls import path
from .views import BookList
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api app URLs
]