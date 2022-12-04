from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.title
