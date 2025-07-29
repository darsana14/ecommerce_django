from django.contrib import admin

from .models import Products

# Register your models here.
admin.site.register(Products) # only when the model is added here, it will be visible for migration