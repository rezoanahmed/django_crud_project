from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def add(request):
    return render(request, 'myapp/add.html')

def info(request):
    return render(request, 'myapp/info.html')

def update(request):
    return render(request, 'myapp/update.html')

def delete(request):
    return render(request, 'myapp/delete.html')

