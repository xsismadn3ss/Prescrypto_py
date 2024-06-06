from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from Prescrypto.auth_model import auth


# Create your views here.
def home(request):
    return render(request, "home.html", {"home_data:":auth.description, "auth": auth.state})

def prescriptions(request):
    template = loader.get_template("prescriptions.html")
    return HttpResponse(template.render())

def recetas(reques):
    template = loader.get_template("recetas.html")
    return HttpResponse(template.render())

def test(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())

def memebers(request):
    return HttpResponse("hello world")