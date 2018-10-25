from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Book, Wisesaying

class IndexView(TemplateView):
    template_name = 'reading/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_num = Book.objects.count()
        Wisesaying_num = Wisesaying.objects.count()
        context['data'] = {'book_num':book_num, 'Wisesaying_num':Wisesaying_num}
        return context

class ListsView(ListView):
    model = Book

class WisesayingDetailView(DetailView):
    model = Wisesaying
