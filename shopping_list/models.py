from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(
        max_digits=18, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)]  # Ensures price is positive
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class shoppinglist(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id_product.name}"