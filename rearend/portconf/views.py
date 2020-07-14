from django.shortcuts import render

# Create your views here.

def tables(request):
    return render(request,'home/tables.html')

def tables_dynamic(request):
    return render(request,'home/tables_dynamic.html')