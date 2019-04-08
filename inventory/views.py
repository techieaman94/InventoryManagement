from django.shortcuts import render, get_object_or_404
from django.shortcuts import Http404
from django.http import HttpResponse
from django.shortcuts import redirect

import json
from django.forms.models import model_to_dict

# Create your views here.
from .forms import login_form , Inventory_add_Form_for_manager, Inventory_add_Form_for_assistant
from .models import Inventory_Records


reques_for_permission = False

permission_for_assistant = {
	'add'		: False,
	'change' 	: False,
	'delete'	: False
}



def home_view(request):
	if not request.user.is_authenticated:

		return render(request, 'inventory/home.html',{})
	else:
		return redirect ('/imsys')

			
	'''
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        else:
            return redirect('students:quiz_list')
    '''
def login_view(request):

	if request.user.is_Manager:

		context={}
		return render(request,'inventory/login_manager_view.html',context)

	elif request.user.is_Assistant:
		#return render(request, 'inventory/login_assistant_view.html',{})
		return render(request,'inventory/login_assistant_view.html',{})

           
            
def inventory_add_view(request):

	if request.user.is_authenticated:
		if request.user.is_Manager:
			form = Inventory_add_Form_for_manager(request.POST or None)
			if form.is_valid():
				form.save()
				return redirect('/imsys/')
				form = Inventory_add_Form_for_manager()
			context={
			'form': form
			}

			return render(request,"inventory/inventory_create.html",context)

		elif request.user.is_Assistant:
			form = Inventory_add_Form_for_assistant(request.POST or None)
			if form.is_valid():
				form.save()
				return redirect('/imsys/')
				form = Inventory_add_Form_for_assistant()
			context={
			'form': form
			}

			return render(request,"inventory/inventory_create.html",context)

			#return HttpResponse("<h2> Assistant !!!  You require permission of a manager to make any change in inventory records</h2>")
	
	else:
		return HttpResponse("<h2> Hello!!!  You are not authorized to Add / change / delete Inventory records</h2>")




def inventory_fetch_view(request):

	if request.user.is_authenticated:
		if request.user.is_Manager:
				
			records = Inventory_Records.objects.filter(Status='Pending')
			context={ 
				'records_pending' : records
				}

			return render(request,"inventory/pending_records.html",context)

			#return HttpResponse("<h2> Fetch and Approve page</h2>")


	else:
		return HttpResponse("<h2> Hello!!!  You are not authorized to Add / change / delete Inventory records</h2><h2> login to continue</h2>")





def inventory_approve_view(request , id=id):

	if request.user.is_authenticated:
		if request.user.is_Manager:
			obj= get_object_or_404(Inventory_Records , id = id)
			form = Inventory_add_Form_for_manager(request.POST or None , instance=obj)
			if form.is_valid():
				form.save()
				return redirect('/inventory/allrecords/')
				#form = Inventory_add_Form_for_manager()
			context={
			'form': form
			}


			return render(request,"inventory/inventory_create.html",context) 
			
		elif request.user.is_Assistant:
			return HttpResponse("<h2> Assistant !!!  You require permission of a manager to make any change in inventory records</h2>")
	
	else:
		return HttpResponse("<h2> Hello!!!  You are not authorized to Add / change / delete Inventory records</h2>")




def inventory_change_view(request):

	if request.user.is_authenticated:

				
		records = Inventory_Records.objects.all()
			
		context={ 
			'records' : records
			}

		return render(request,"inventory/all_records.html",context)

			#return HttpResponse("<h2> Fetch and Approve page</h2>")


	else:
		return HttpResponse("<h2> Hello!!!  You are not authorized to Add / change / delete Inventory records</h2><h2> login to continue</h2>")




def inventory_change_record_view(request,id=id):

	if request.user.is_authenticated:
		if request.user.is_Manager:
			obj= get_object_or_404(Inventory_Records , id = id)
			form = Inventory_add_Form_for_manager(request.POST or None , instance=obj)
			if form.is_valid():
				form.save()
				return redirect('/inventory/allrecords/')

				#form = Inventory_add_Form_for_manager()
			context={
			'form': form
			}

			return render(request,"inventory/inventory_create.html",context)  

		elif request.user.is_Assistant:

			obj= get_object_or_404(Inventory_Records , id = id)
			form = Inventory_add_Form_for_assistant(request.POST or None , instance=obj)
			if form.is_valid():
				form.save()
				return redirect('/inventory/allrecords/')

				#form = Inventory_add_Form_for_manager()
			context={
			'form': form
			}

			return render(request,"inventory/inventory_create.html",context)  

			#return HttpResponse("<h2> Assistant !!!  You require permission of a manager to make any change in inventory records</h2>")
	
	else:
		return HttpResponse("<h2> Hello!!!  You are not authorized to Add / change / delete Inventory records</h2>")




def inventory_delete_record_view(request,id=id):

	if request.user.is_authenticated:
		if request.user.is_Manager:
			obj= get_object_or_404(Inventory_Records , id = id)
			
			
			obj.delete()
			return redirect('/inventory/allrecords/')

		elif request.user.is_Assistant:
			return HttpResponse("<h2> Assistant !!!  You are NOT ALLOWED !! to delete inventory records</h2>")
	
	else:
		return HttpResponse("<h2> Hello!!!  You are not authorized to Add / change / delete Inventory records</h2>")