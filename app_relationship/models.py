from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(
        'Student',
        related_name='courses'
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name