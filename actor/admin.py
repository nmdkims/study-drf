# admin.py
from django.contrib import admin
from actor.models import Actor, Category

admin.site.register(Actor)
admin.site.register(Category)
