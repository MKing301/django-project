from django.contrib import admin
from .models import BookCategory, Book
from django.db import models


# Register your models here.
admin.site.register(BookCategory)
admin.site.register(Book)