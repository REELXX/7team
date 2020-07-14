from django.shortcuts import render


# Create your views here.


def form_wizards(request):
    return render(request, 'home/form_wizards.html')


def form_upload(request):
    return render(request, 'home/form_upload.html')


def form_buttons(request):
    return render(request, 'home/form_buttons.html')
