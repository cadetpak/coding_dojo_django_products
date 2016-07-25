from django.db import models
from datetime import datetime

class Brand(models.Model):
	brand_name = models.TextField(max_length=50)
	def __str__(self):
		return self.brand_name
	class Meta:
		db_table = 'brands'

class Product(models.Model):
	brand = models.ForeignKey(Brand)
	name = models.TextField(max_length=75)
	price = models.FloatField(default=1.00)
	date_added = models.DateTimeField(auto_now_add=True)
	description = models.TextField(max_length=200)
	def __str__(self):
		return self.name 
	class Meta:
		db_table = 'products'




