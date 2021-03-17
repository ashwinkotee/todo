from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import *
from .forms import *





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

def delete(request,id):
    todo_item = Task_Table.objects.get(id=id)

    todo_item.delete()

    return redirect('/')

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





    