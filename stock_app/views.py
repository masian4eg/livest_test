from .models import GroupsOfProducts, CategoriesOfProducts, Products
from .serializers import GroupsSerializer, CategoriesSerializer, ProductsSerializer

from rest_framework import generics


class GroupsAPIListCreate(generics.ListCreateAPIView):
    queryset = GroupsOfProducts.objects.all()
    serializer_class = GroupsSerializer


class GroupsAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupsOfProducts.objects.all()
    serializer_class = GroupsSerializer


class CategoriesAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriesOfProducts.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesAPIListCreate(generics.ListCreateAPIView):
    queryset = CategoriesOfProducts.objects.all()
    serializer_class = CategoriesSerializer


class ProductsAPIListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    search_fields = ['name']
