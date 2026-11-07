from django.contrib import admin
from .models import Profile, Category, Product, Course, Student

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Course)
admin.site.register(Student)