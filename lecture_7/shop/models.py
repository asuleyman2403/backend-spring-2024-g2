from django.db import models


class Category(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'ID: {self.id} {self.name}'


class Product(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)
    description = models.CharField(null=False, max_length=2000, blank=True, default='')
    price = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now=True, null=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'ID: {self.id} {self.name}'


# Category - Categories - Categorys


