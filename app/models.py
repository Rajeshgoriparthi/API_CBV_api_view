from django.db import models

# Create your models here.


class Product_catagiry(models.Model):
    pc_id=models.IntegerField()
    pc_name=models.CharField(max_length=500)

    def __str__(self):
        return self.pc_name


class Product(models.Model):
    pc_name=models.ForeignKey(Product_catagiry,on_delete=models.CASCADE)
    p_id=models.IntegerField()
    p_name=models.CharField(max_length=100)
    p_price=models.CharField(max_length=10)
    p_description=models.TextField()
    p_date=models.DateField()
    


    def __str__(self):
        return self.p_name