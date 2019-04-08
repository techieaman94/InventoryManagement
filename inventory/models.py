from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import AbstractUser

#from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_Assistant = models.BooleanField(default=False)
    is_Manager = models.BooleanField(default=False)








class Inventory_Records(models.Model):

	STATUS_CHOICES = [
    ("Pending", "Pending"),
    ('Approved' , 'Approved'),
	]

	Product_id 			=	models.CharField(max_length=20) 
	Product_Name		=	models.CharField(max_length=100)
	Vendor				=	models.CharField(max_length=150)
	MRP					=	models.DecimalField(decimal_places=2,max_digits=15)
	Batch_Number		=	models.IntegerField() 
	Batch_Date			=	models.DateField()
	Quantity_in_Hand	=	models.IntegerField() 
	Status				=	models.CharField(max_length=30,choices=STATUS_CHOICES,default="Pending")

	
	'''
	def get_absolute_url(self):
		return reverse("inventory:inventory-create", kwargs={"id": self.id})

	
	def get_absolute_url(self):
		#return f"/employee/{self.id}/"
		return reverse("inventory_approve_view",kwargs={"id": self.id})
	'''

