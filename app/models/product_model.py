from django.db import models
from django.utils import timezone


class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"
