from django.urls import path
from .views import (
    BookCitationsView,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

app_name = 'books'

urlpatterns = [
    path('citations/', BookCitationsView.as_view(), name='citation_kolymb'),
    path('book/', BookListView.as_view(), name='book_user'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
    path('create_book/', BookCreateView.as_view(), name='new_book_user'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='update_book'),
]