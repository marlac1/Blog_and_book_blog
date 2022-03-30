from django.db import models

# Create your models here.

class Author(models.Model):
    #firstname, lastname, wikipedia
    firstname = models.CharField(max_length = 50, blank=False)
    lastname = models.CharField(max_length = 50, blank=False)
    wikipedia = models.URLField(blank=True, default="")
    test = models.CharField(max_length=22, default="")

    def __str__(self):
        return f"L'auteur s'appelle {self.firstname} {self.lastname}"


class Book(models.Model):
    TYPE_BOOKS = (
        ("1", "Aventure"),
        ("2", "Thriller"),
        ("3", "Fantastique"),
        ("4", "Romance"),
        ("5", "Horreur"),
        ("6", "Science-fiction")
    )
    title = models.CharField(max_length=100) #parametre obligatoire de longueur max
    price = models.DecimalField(blank=True, null=False, max_digits=2, decimal_places=2)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(
        max_length=100,
        choices=TYPE_BOOKS,
        blank=True
    )
    tests = models.CharField(max_length=2, default="")
    def __str__(self):
        return f"Voici le titre du livre : {self.title}"




