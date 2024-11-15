from django.shortcuts import render


def header(request):
    print("Rendering header.html")
    return render(request, 'header.html')

def index(request):
    return render(request, 'index.html')

def homePage(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Experience(request):
    return render(request, 'Experience.html')

def Projects(request):
    return render(request, 'projects.html')


