# Generated by Django 4.0.4 on 2022-04-24 05:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesOfProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('seq', models.IntegerField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'CategoryOfProducts',
                'verbose_name_plural': 'CategoriesOfProducts',
            },
        ),
        migrations.CreateModel(
            name='GroupsOfProducts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('seq', models.IntegerField(blank=True, unique=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_app.categoriesofproducts')),
            ],
            options={
                'verbose_name': 'GroupOfProducts',
                'verbose_name_plural': 'GroupsOfProducts',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hidden', models.BooleanField(default=False)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock_app.groupsofproducts')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]