import random

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL
# Create your models here.
class Product(models.Model):
    TAGS_LIST = ['fruits', 'voiture', 'electronique']
    # on_delete : si on supprime l'utilisateur le produit reste avec un user = null
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    public = models.BooleanField(default=True)
    def get_tags_list(self):
        return [random.choice(self.TAGS_LIST)]
    def is_public(self) -> bool:
        return self.public
    @property
    def get_discount(self):

        return "%.2f"%(float(self.price) * 0.5)
    def __str__(self):
        return self.name