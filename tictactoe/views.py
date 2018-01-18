from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hello, World!")


def index(request):
    return HttpResponse("on index")