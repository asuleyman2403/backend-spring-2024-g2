from django.db import models


class Product(models.Model):
    name = models.CharField(null=False, max_length=255, blank=False)
    description = models.CharField(null=False, max_length=2000, blank=True, default='')
    price = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'ID: {self.id} {self.name}'


# Category - Categories - Categorys


