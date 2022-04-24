from django.db import models
import uuid


class CategoriesOfProducts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    seq = models.IntegerField(blank=True, unique=True)

    class Meta:
        verbose_name = 'CategoryOfProducts'
        verbose_name_plural = 'CategoriesOfProducts'

    def __str__(self):
        return self.name


class GroupsOfProducts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    category_id = models.ForeignKey(CategoriesOfProducts, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    description = models.TextField()
    seq = models.IntegerField(blank=True, unique=True)

    class Meta:
        verbose_name = 'GroupOfProducts'
        verbose_name_plural = 'GroupsOfProducts'

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(GroupsOfProducts, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
