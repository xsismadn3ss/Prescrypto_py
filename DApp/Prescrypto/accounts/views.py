from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from Prescrypto.models import Users
# from Prescrypto.forms import UserForm
from Prescrypto.auth_model import auth
import hashlib

def hash_password(password):
    password_bytes = password.encode("utf-8")
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password

def check_auth_state(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if auth.state:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return _wrapped_view_func

#views
def login(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            myuser = Users.objects.get(username=username, password=password)

            if myuser.username == username and myuser.password == password is not None:
                print(True)
                data = auth.description = f"Bienvenido {username}"
                auth.state = True
                return HttpResponseRedirect("/", {"auth":auth.state})
        except Exception as e:
            print(e)  
            data = "Datos incorectos ⚠️"
            return render(request, "core/login.html", {"data":data, "auth":auth.state})
    return render(request, "core/login.html", {"auth":auth.state})

def logout(request):
    template = loader.get_template("core/logout.html")
    return HttpResponse(template.render())


def create_account(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        dui = request.POST.get("dui")
        username = request.POST.get("username")
        wallet = request.POST.get("wallet")
        pk = request.POST.get("pk")
        password = request.POST.get("password")
        confirm = request.POST.get("password_c")

        if password == confirm:
            try:
                add_user = Users(
                    firstname = name,
                    lastname  = lastname,
                    username = username,
                    dui = dui,
                    wallet = wallet,
                    private_key = pk,
                    password = password
                )
                add_user.save()

            except Exception as e:
                if str(e) == "UNIQUE constraint failed: Prescrypto_users.username":
                    return render(
                        request, 
                        "core/create_account.html",
                        {"data": "*El nombre de usuario ya existe*"}
                    )
                if str(e) == "UNIQUE constraint failed: Prescrypto_users.dui":
                    return render(
                        request, 
                        "core/create_account.html",
                        {"data": "*El DUI que deseas ingresar ya esta registrado*"}
                    )
                if str(e) == "UNIQUE constraint failed: Prescrypto_users.private_key":
                    return render(
                        request, 
                        "core/create_account.html",
                        {"data": "*Asegurate de pegar la claver privada correcta*"}
                    )
                if str(e) == "UNIQUE constraint failed: Prescrypto_users.wallet":
                    return render(
                        request, 
                        "core/create_account.html",
                        {"data": "*Esta billetera de ethereum ya esta registrada*"}
                    )
        else:
            return render(request, "core/create_account.html", {"data":"*La contraseña no coincide*"})
    else:
        return render(request, "core/create_account.html")