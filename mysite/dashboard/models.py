from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    age = models.SmallIntegerField(blank=False,null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=100, null=False,blank=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False,null=False)
    description = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title