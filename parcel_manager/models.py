from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.brand}"

class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    sender = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Confirmed", "Confirmed"),
            ("In delivery", "In delivery"),
            ("Delivered", "Delivered"),
        ],
        default="Confirmed",
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders", default=1)
    #models.ManyToManyField(Product)  # Relation ManyToMany

    def __str__(self):
        return f"Order N°{self.id} : {self.sender} to {self.destination} - {self.status}"