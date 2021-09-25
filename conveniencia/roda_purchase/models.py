import uuid
from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    sku = models.CharField(max_length=7, unique=True, default=uuid.uuid4, editable=False)
    product = models.ManyToManyField(Product, related_name="purchased")     # Many to Many field
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sku)
