from django import forms

from .models import Inventory_Records

class login_form( forms.ModelForm):
	username				= forms.CharField()
	
	password				= forms.CharField()
	
	

	
	class Meta:
		model = Inventory_Records
		fields = [
			'username',
			'password',
		]



status_choices_for_manager 		= (
			('Approved' , 'Approved'),
		)


status_choices_for_assistant 		= (
			('Pending' , 'Pending'),
		)


class Inventory_add_Form_for_manager( forms.ModelForm):
	
	Product_id 			=	forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder" : "Enter the Product ID "})) 
	Product_Name		=	forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Enter the Product Name "}))
	Vendor				=	forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder" : "Enter the Vendor Name "}))
	MRP					=	forms.DecimalField(decimal_places=2,max_digits=15)
	Batch_Number		=	forms.IntegerField() 
	Batch_Date			=	forms.DateField()
	Quantity_in_Hand	=	forms.IntegerField() 

	
	Status				=	forms.ChoiceField(
											choices=status_choices_for_manager
											)


	class Meta:
		model = Inventory_Records
		fields = [
			'Product_id',
			'Product_Name',
			'Vendor',
			'MRP',
			'Batch_Number',
			'Batch_Date',
			'Quantity_in_Hand',
			'Status',
		]


class Inventory_add_Form_for_assistant( forms.ModelForm):
	
	Product_id 			=	forms.CharField(max_length=20, widget=forms.TextInput(attrs={"placeholder" : "Enter the Product ID "})) 
	Product_Name		=	forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Enter the Product Name "}))
	Vendor				=	forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder" : "Enter the Vendor Name "}))
	MRP					=	forms.DecimalField(decimal_places=2,max_digits=15)
	Batch_Number		=	forms.IntegerField() 
	Batch_Date			=	forms.DateField()
	Quantity_in_Hand	=	forms.IntegerField() 

	
	Status				=	forms.ChoiceField(
											choices=status_choices_for_assistant
											)


	class Meta:
		model = Inventory_Records
		fields = [
			'Product_id',
			'Product_Name',
			'Vendor',
			'MRP',
			'Batch_Number',
			'Batch_Date',
			'Quantity_in_Hand',
			'Status',
		]