from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    pages = models.IntegerField()
    edition = models.CharField()
    release_date = models.DateTimeField()
    rating = models.FloatField(max_length=5)
    description = models.TextField()
    genre = models.ExpressionList()
    cover = models.ImageField()

    