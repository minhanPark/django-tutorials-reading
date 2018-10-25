from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    introduction = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Wisesaying(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
