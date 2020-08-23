from django.shortcuts import render


def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def aboutUs(request):
    if request.method == 'GET':
        return render(request, 'about.html')


def contactUs(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
