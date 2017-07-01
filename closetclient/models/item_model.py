from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone


class Category(models.Model):
    """ adds a Category model to our SQLite database """
    category_name = models.CharField(max_length=50)

    # returns human readable string
    def __str__(self): # only if you need to support Python 2
        return self.category_name

    
    def get_items(self):
        print(dir(self))
        return Item.objects.filter(category_type=self)


class Item(models.Model):
    """ adds an Item model to our SQLite database """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # django will display a dropdown with these choices
    CATEGORY_CHOICES = (
        ('tops', 'TOPS'),
        ('bottoms', 'BOTTOMS'),
        ('outerwear', 'OUTERWEAR'),
        ('bags', 'BAGS'),
        ('shoes', 'SHOES'),
        ('accessories', 'ACCESSORIES'),
        ('jewelry', 'JEWELRY'))

    category_type = models.ForeignKey(Category, on_delete=models.CASCADE, choices=CATEGORY_CHOICES)
    item_name = models.CharField(max_length=200)
    item_count = models.IntegerField(default=0)
    color = models.CharField(max_length=200)
    date_created = models.DateField(auto_now=True, auto_now_add=False)  # This auto generates date on creation

    # returns human readable string
    def __str__(self): # only if you need to support Python 2
        return self.item_name
