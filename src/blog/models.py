from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import json
import itertools
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=56)
    slug = models.SlugField()

    def __str__(self):
        return self.name



class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()
    other = models.TextField(blank=True, null=True)

    @property
    def published_string(self):
        if self.published:
            return f"article publié"
        return f"article inaccessible"

    @property
    def number_of_words(self):
        return len(self.content.split())

    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug" : self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.date}"

    @property
    def word_count(self):
        return len(self.content.split())

    class Meta:
        verbose_name="Article"
        ordering=["-date"]


