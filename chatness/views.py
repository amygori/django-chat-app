from django.shortcuts import render


def index(request):
    return render(request, "chatness/index.html")
