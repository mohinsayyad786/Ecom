from django.db import models

# Create your models here.
class Task(models.Model):
    product_id=models.CharField(max_length=50)
    product_name=models.CharField(max_length=500)
    product_shape=models.CharField(max_length=50)
    product_size=models.CharField(max_length=500)
    product_location=models.CharField(max_length=50)
    product_price=models.CharField(max_length=500)
    is_deleted=models.CharField(max_length=10)
  