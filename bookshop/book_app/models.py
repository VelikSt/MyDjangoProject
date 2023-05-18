from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=70)         #Название книги
    rating = models.IntegerField()                  #Рейтинг книги
    year = models.IntegerField()
    budget = models.IntegerField()
    def __str__(self):
        books = f'{self.title} - {self.rating}%'
        return books