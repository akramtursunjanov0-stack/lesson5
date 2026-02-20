from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import Book
from .forms import BookForm



class BookCitationsView(View):
    def get(self, request):
        return HttpResponse("Страница цитат")



class BookListView(ListView):
    model = Book
    template_name = 'book/book.html'
    context_object_name = 'book'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('s')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query)
            )
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book_id'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_url = reverse_lazy('books:book_user')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/update_book.html'
    context_object_name = 'book_id'
    success_url = reverse_lazy('books:book_user')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/confirm_delete.html'
    success_url = reverse_lazy('books:book_user')