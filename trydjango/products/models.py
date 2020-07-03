from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    features    = models.BooleanField(default=False) # null=True, default=True

    def get_absolute_url(self):
        # products: is a way to change namespace. here app_name is products set in urls.py
        return reverse("products:product-detail", kwargs={"id": self.id}) # classic easy way to make sure urls are dynamic
        # return f"/products/{self.id}/"