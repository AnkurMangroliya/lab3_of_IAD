from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Publisher, Book, Member, Order
from django.shortcuts import get_object_or_404
from django.shortcuts import render
<<<<<<< HEAD
from .forms import FeedbackForm
from .forms import SearchForm
=======
from django.shortcuts import render
>>>>>>> ce204b837a20845cd59a0f8bbd40be31aa47f5fc

def home(request):
    return render(request, 'home.html')

def about(request):
<<<<<<< HEAD
    return render(request, 'myapp/about.html')
=======
    return render(request, 'myapp/about0.html')
>>>>>>> ce204b837a20845cd59a0f8bbd40be31aa47f5fc


def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
<<<<<<< HEAD
    return render(request, 'myapp/index.html', {'booklist': booklist})

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'myapp/detail.html', {'book': book})

def getFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            if feedback == 'B':
                choice = ' to borrow books.'
            elif feedback == 'P':
                choice = ' to purchase books.'
            else: choice = ' None.'
            return render(request, 'myapp/fb_results.html', {'choice':choice})
        else:
            return HttpResponse('Invalid data')
    else:
        form = FeedbackForm()
        return render(request, 'myapp/feedback.html', {'form':form})

def findbooks(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            max_price = form.cleaned_data['max_price']

            # Querying the database for books
            if category:
                booklist = Book.objects.filter(category=category, price__lte=max_price)
            else:
                booklist = Book.objects.filter(price__lte=max_price)

            return render(request, 'myapp/results.html', {
                'name': name,
                'category': category,
                'booklist': booklist
            })
        else:
            return HttpResponse('Invalid data')
    else:
        form = SearchForm()
        return render(request, 'myapp/findbooks.html', {'form': form})
=======
    return render(request, 'myapp/index0.html', {'booklist': booklist})
>>>>>>> ce204b837a20845cd59a0f8bbd40be31aa47f5fc
