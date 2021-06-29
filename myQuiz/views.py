from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render()


def about(request):
    return HttpResponse("<h4>PAGE ABOUT</h4>")
