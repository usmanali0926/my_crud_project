from django.shortcuts import render,HttpResponseRedirect
from my_crud_app.models import Student
from my_crud_app.forms import StudentForm
from django.contrib import messages


# Create your views here.


# this function will add new item and show all item
def add_show(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    else:
        form = StudentForm()
    students = Student.objects.all()
    return render(request, 'addandshow.html',{'form':form,'student': students})


# this function is used for edit the data

def edit_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
    fm = StudentForm(instance=pi)
    return render(request, 'update.html', {'form': fm})


# this function for delete

def delete_data(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
