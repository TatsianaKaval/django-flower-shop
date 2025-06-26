from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='uploads')
    description = models.TextField(default="All our flowers are collected only after your order, which guarantees the freshness of the bouquets. For you, with love!")

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, default="+375", help_text="*In the format +375 xx xxx xx xx")
    email = models.EmailField(blank=True, null=True, help_text="*The field is optional")
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    apartment = models.IntegerField(blank=True, null=True, help_text="*The field is optional")
    inscription = models.TextField(max_length=1000, default="Congratulation!", help_text="*The text on the postcard")
    product = models.ForeignKey('Products', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name