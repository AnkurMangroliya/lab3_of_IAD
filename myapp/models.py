from django.db import models

from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# Publisher model with the new 'country' field
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, default='USA')

    def str(self):
        return self.name

# Book model with the new 'description' field
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('S', 'Scinece&Tech'),
        ('F', 'Fiction'),
        ('B', 'Biography'),
        ('T', 'Travel'),
        ('O', 'Other')
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='S')
    num_pages = models.PositiveIntegerField(default=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def str(self):
        return self.title

# Member model
class Member(User):
    STATUS_CHOICES = [
        (1, 'Regular member'),
        (2, 'Premium member'),
        (3, 'Guest member'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, default='ON')
    last_renewal = models.DateField(default=timezone.now)
    auto_renew = models.BooleanField(default=True)
    borrowed_books = models.ManyToManyField('Book', blank=True)

    def str(self):
        return self.username

# Order model
class Order(models.Model):
    ORDER_CHOICES = [
        (0, 'Purchase'),
        (1, 'Borrow'),
    ]
    books = models.ManyToManyField(Book)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    order_type = models.IntegerField(choices=ORDER_CHOICES, default=1)
    order_date = models.DateField(default=timezone.now)

    def str(self):
        return f"Order by {self.member.username} on {self.order_date}"

    def total_items(self):
        return self.books.count()