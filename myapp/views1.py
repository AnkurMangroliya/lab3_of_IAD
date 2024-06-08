# Import necessary classes
from django.http import HttpResponse
from .models import Publisher, Book, Member, Order
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    response = HttpResponse()
    booklist = Book.objects.all().order_by('title')[:10]
    heading1 = '<p>' + 'List of available books: ' + '</p>'
    response.write(heading1)
    for book in booklist:
        para = '<p>'+ str(book.id) + ': ' + str(book) + '</p>'
        response.write(para)

    # List of publishers sorted by city name in descending order
    publisherlist = Publisher.objects.all().order_by('city')
    heading2 = '<p>' + 'List of publishers: ' + '</p>'
    response.write(heading2)
    for publisher in publisherlist:
        para = '<p>' + str(publisher.name) + ': ' + str(publisher.city) + '</p>'
        response.write(para)
    return response

def about(request):
    return HttpResponse("This is an eBook APP.")

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    response = HttpResponse()
    heading = '<h1>' + book.title.upper() + '</h1>'
    response.write(heading)
    price = '<p>' + 'Price: $' + str(book.price) + '</p>'
    response.write(price)
    publisher = '<p>' + 'Publisher: ' + str(book.publisher) + '</p>'
    response.write(publisher)
    return response