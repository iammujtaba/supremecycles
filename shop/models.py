from base.models import BaseModel
from django.db import models
from shop.choices import BicycleCategory, BicycleSize, BicycleBrand, BicycleAccessoriesCategory, BicycleAccessoriesBrand


class Bicycle(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=30, choices=BicycleSize.choices, validators=[BicycleSize.validator])
    color = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, choices=BicycleBrand.choices, validators=[BicycleBrand.validator])
    sub_brand = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=30, choices=BicycleCategory.choices, validators=[BicycleCategory.validator])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_id = models.CharField(max_length=100,null=True,blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class BicycleAccessories(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=30, choices=BicycleAccessoriesCategory.choices, validators=[BicycleAccessoriesCategory.validator])
    brand = models.CharField(max_length=30, choices=BicycleAccessoriesBrand.choices, validators=[BicycleAccessoriesBrand.validator])
    sub_brand = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    size = models.CharField(max_length=30, choices=BicycleSize.choices, validators=[BicycleSize.validator])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_id = models.CharField(max_length=100,null=True,blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
