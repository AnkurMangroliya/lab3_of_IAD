# Import necessary classes
from django.http import HttpResponse
from .models import Publisher, Book, Member, Order

# Create your views here.
def index(request):
    response = HttpResponse()
    booklist = Book.objects.all().order_by('title')[:10]
    heading1 = '<p>' + 'List of available books: ' + '</p>'
    response.write(heading1)
    for book in booklist:
        para = '<p>'+ str(book.id) + ': ' + str(book) + '</p>'
        response.write(para)
    return response
