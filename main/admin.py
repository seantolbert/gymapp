from django.contrib import admin
from .models import Category, Tag, Exer, Workout

admin.site.register(Workout)
admin.site.register(Category)
admin.site.register(Exer)
admin.site.register(Tag)
