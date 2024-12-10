from django.shortcuts import render

def index(request):
    return render(request, "curso/index.html")

def about(request):
    return render(request, "curso/about.html")


