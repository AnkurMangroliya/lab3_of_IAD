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
    return render(request, 'myapp/about0.html')


def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index0.html', {'booklist': booklist})