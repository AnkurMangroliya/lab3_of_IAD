from django.shortcuts import render
from .forms import ReviewForm
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
from .models import Publisher, Book, Member, Order
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render
from .forms import FeedbackForm, SearchForm, OrderForm

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

def getFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.cleaned_data['feedback']
            return render(request, 'myapp/fb_results.html', {'feedback': feedback})
    else:
        form = FeedbackForm()
    return render(request, 'myapp/feedback.html', {'form': form})

def findbooks(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            max_price = form.cleaned_data['max_price']
            if category:
                booklist = Book.objects.filter(category=category, price__lte=max_price)
            else:
                booklist = Book.objects.filter(price__lte=max_price)
            return render(request, 'myapp/results.html', {'name': name, 'category': category, 'booklist': booklist})
        else:
            return HttpResponse('Invalid data')
    else:
        form = SearchForm()
        return render(request, 'myapp/findbooks.html', {'form': form})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            books = form.cleaned_data['books']
            order = form.save(commit=False)
            member = order.member
            order_type = order.order_type
            order.save()
            if order_type == 1:
                for b in order.books.all():
                    member.borrowed_books.add(b)
            return render(request, 'myapp/order_response.html', {'books': books, 'order': order})
        else:
            return render(request, 'myapp/placeorder.html', {'form': form})
    else:
        form = OrderForm()
        return render(request, 'myapp/placeorder.html', {'form': form})

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            if 1 <= rating <= 5:
                review = form.save()
                book = review.book
                book.num_reviews += 1
                book.save()
                return redirect('myapp:index')
            else:
                form.add_error('rating', 'You must enter a rating between 1 and 5!')
    else:
        form = ReviewForm()
    return render(request, 'myapp/review.html', {'form': form})