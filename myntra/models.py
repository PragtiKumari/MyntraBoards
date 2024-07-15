from django.db import models

# Create your models here.

class Wishlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    original_price = models.IntegerField()
    discounted_price = models.IntegerField()
    offer = models.IntegerField()
    image_path = models.CharField(max_length=355)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class mysavereel(models.Model):
    path=models.CharField(max_length=355)
    
    def __str__(self):
        return self.path
    
    
    
    
