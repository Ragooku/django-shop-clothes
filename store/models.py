from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото товара')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    is_available = models.BooleanField(default=True, verbose_name='Акутальность')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'code': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название категории')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото товара')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'category_code': self.pk})


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    city = models.CharField(max_length=20, verbose_name='Город')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
