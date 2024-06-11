from re import template
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
                data = auth.description = f"{username}"
                print(myuser.dui)
                auth.id = myuser.dui
                print(auth.id)
                auth.state = True
                return HttpResponseRedirect("/", {"auth":auth.state})
        except Exception as e:
            print(e)  
            data = "Datos incorectos ⚠️"
            return render(request, "core/login.html", {"data":data, "auth":auth.state})
    return render(request, "core/login.html", {"auth":auth.state})

def logout(request):
    template = "core/logout.html"
    if request.method == "POST" and auth.state == True:
        # estado = auth.state = False
        yes = request.POST.get("Si")
        no = request.POST.get("No")
        
        if yes == "ok":
            auth.state = False
            auth.id = None
            print(f"sesión finalizada ({auth.description})")
            auth.description = ""
            return HttpResponseRedirect("/", {"auth": auth.state})
        
        if no == "cancel":
            auth.state = True
            return HttpResponseRedirect("/", {"auth":auth.state})
    else:
        return render(request, template, {"auth": auth.state})

    return render(request, template)


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
                print(e)
                # return render(
                #     request, "core/create_account.html", {}
                # )
                if str(e) == "UNIQUE constraint failed: Prescrypto_users.username":
                    return render(
                        request, 
                        "core/create_account.html",
                        {
                            "data": "*El nombre de usuario ya existe*",
                            "name": name,
                            "lastname": lastname,
                            # "username": username,
                            "dui": dui,
                            "wallet": wallet,
                            "pk": pk,
                            "password": password,
                            "password_c": confirm
                        }
                    )
                elif str(e) == "UNIQUE constraint failed: Prescrypto_users.dui":
                    return render(
                        request, 
                        "core/create_account.html",
                        {
                            "data": "*El DUI que deseas ingresar ya esta registrado*",
                            "name": name,
                            "lastname": lastname,
                            "username": username,
                            # "dui": dui,
                            "wallet": wallet,
                            "pk": pk,
                            "password": password,
                            "password_c": confirm
                        }
                    )
                elif str(e) == "UNIQUE constraint failed: Prescrypto_users.wallet" or "UNIQUE constraint failed: Prescrypto_users.private_key":
                    return render(
                        request, 
                        "core/create_account.html",
                        {
                            "data": "*Esta billetera de ethereum ya esta registrada*",
                            "name": name,
                            "lastname": lastname,
                            "username": username,
                            "dui": dui,
                            # "wallet": wallet,
                            # "pk": pk,
                            "password": password,
                            "password_c": confirm
                        }
                    )
        else:
            return render(
                request, "core/create_account.html", 
                {
                    "data":"*La contraseña no coincide*", 
                    "auth": auth.state,
                    "name": name,
                    "lastname": lastname,
                    "username": username,
                    "dui": dui,
                    "wallet": wallet,
                    "pk": pk,
                    # "password": password,
                    # "password_c": confirm
                }
            )
    else:
        return render(request, "core/create_account.html", {"auth": auth.state})
    
def account_details(request):
    template = "core/account.html"
    user = Users.objects.get(dui=f"{auth.id}")
    # print(user.firstname)
    context = {
        "user": user,
        "auth": auth.state 
    }
    return render(request, template, context=context)