from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publisher, Book

admin.site.register(Publisher)
admin.site.register(Book)
