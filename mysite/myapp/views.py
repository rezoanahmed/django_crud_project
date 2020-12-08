from django.shortcuts import render
from myapp.models import *
from myapp.forms import *
# Create your views here.
def home(request):
    student_list = student.objects.all()
    mydict = {'student_list':student_list}
    return render(request, 'myapp/index.html', context=mydict)



def add(request):
    add_student=student_form()

    if request.method == "POST":
        add_student=student_form(request.POST)

        if add_student.is_valid():
            add_student.save(commit=True)
            return home(request)


    mydict = {'add':add_student}
    return render(request, 'myapp/add.html', context=mydict)



def info(request,student_id):
    student_info = student.objects.get(pk=student_id)
    mydict = {'info':student_info}
    return render(request, 'myapp/info.html',context=mydict)



def update(request,student_id):
    student_list = student.objects.get(pk=student_id)
    update_student = student_form(instance = student_list)
    
    if request.method == "POST":
        update_student = student_form(request.POST, instance= student_list)

        if update_student.is_valid():
            update_student.save(commit=True)
            return home(request)
    
    mydict={'update':update_student}
    return render(request, 'myapp/update.html',context=mydict)



def delete(request,student_id):
    delete_student = student.objects.get(pk=student_id).delete()
    mydict = {'deleted': delete_student}
    return render(request, 'myapp/delete.html', context=mydict)

