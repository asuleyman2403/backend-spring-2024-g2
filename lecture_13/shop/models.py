from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    code = models.CharField(max_length=255, unique=True, null=False)
    category = models.ForeignKey(Category, null=False, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)
