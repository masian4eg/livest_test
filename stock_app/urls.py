from django.urls import path

from .views import *

urlpatterns = [
    path('product-groups/', GroupsAPIListCreate.as_view()),
    path(r'product-groups/<uuid:pk>/', GroupsAPIRetrieveUpdateDestroy.as_view()),
    path('product-categories/', CategoriesAPIListCreate.as_view()),
    path('product-categories/<int:pk>/', CategoriesAPIRetrieveUpdateDestroy.as_view()),
    path('products/', ProductsAPIListCreate.as_view()),
]
