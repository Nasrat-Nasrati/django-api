from django.db import models

# Create your models here.
class Orders(models.Model):
    amount = models.CharField( max_length=50)
    description = models.TextField()
    created_time = models.DateField( auto_now=False, auto_now_add=False)

    

