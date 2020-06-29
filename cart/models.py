
# Create your models here.
from __future__ import unicode_literals

from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    category = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{0} ({1})".format(self.product.name, self.quantity)