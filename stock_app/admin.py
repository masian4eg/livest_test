from django.contrib import admin
from .models import CategoriesOfProducts, GroupsOfProducts, Products

admin.site.register(CategoriesOfProducts)
admin.site.register(GroupsOfProducts)
admin.site.register(Products)
