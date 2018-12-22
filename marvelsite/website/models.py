from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    image = models.ImageField()
    readmore = models.CharField(max_length=200)
    content = RichTextField()

class Contacts(models.Model):
    name  = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()