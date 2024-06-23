from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Publisher, Book, Member, Order
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'myapp/about.html')


def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'booklist': booklist})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'myapp/detail.html', {'book': book})
