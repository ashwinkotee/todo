from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import TaskTableForm, CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def get(request):
	all_todo = Task_Table.objects.all()
	form = TaskTableForm()

	if request.method == 'POST':
		form = TaskTableForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'all_items': all_todo, 'form':form}
	print(all_todo)
	return render(request, 'index.html', context)

@login_required(login_url='login')
def delete(request,id):
	todo_item = Task_Table.objects.get(id=id)

	todo_item.delete()

	return redirect('/')

@login_required(login_url='login')
def update(request,id):
	todo_item = Task_Table.objects.get(id=id)
	form = TaskTableForm(instance=todo_item)

	if request.method == 'POST':
		form = TaskTableForm(request.POST,instance=todo_item)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'item': form}
	return render(request, 'update.html', context)


def register(request):
	if request.user.is_authenticated:
		return redirect("/")
	else:

		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Profile Created for ' + user )
				return redirect("/login")
		else: 
			form = CreateUserForm()
		

	context = {'form':form}
	return render(request, 'register.html', context)




def loginPage(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password) 

		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Username OR password is incorrect')
			# return redirect('/login')
	return render(request, 'login.html')

def logoutPage(request):
	logout(request)
	return redirect('/login')


	