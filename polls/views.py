from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello world you are at polls index")
