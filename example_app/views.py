from django.shortcuts import render

def index(request):
    return render(request, "example_app/index.html")
