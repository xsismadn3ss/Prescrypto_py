from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from Prescrypto.auth_model import auth


# Create your views here.
def home(request):
    return render(request, "home.html", {"home_data:":auth.description, "auth": auth.state})

def recetas(request):
    template = "recetas.html"
    return render(request, template, {"auth": auth.state})

def prescriptions(request):
    template = "prescriptions.html"
    return render(request, template, {"auth": auth.state})


def test(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())

def memebers(request):
    return HttpResponse("hello world")