from django.urls import path
from django.urls import include
from .views import BookList
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api app URLs
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
