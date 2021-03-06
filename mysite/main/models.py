from django.db import models


# Create your models here.
class BookCategory(models.Model):
    category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)
    category_img_loc = models.FileField(upload_to='mysite/images')

    class Meta:
        verbose_name_plural = "BookCategories"

    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    published_date = models.DateField('date published')
    book_slug = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, verbose_name="Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title