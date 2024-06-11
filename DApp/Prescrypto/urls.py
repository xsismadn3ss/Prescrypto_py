from django.urls import path
from .accounts import views as account_view
from . import views


urlpatterns = [

    #contenido
    path('', view=views.home, name='home'),
    path('recetas',view=views.recetas, name='recetas'),
    path('prescriptions/', view=views.prescriptions, name="prescriptions"),
    

    #cuentas
    path('login/', view=account_view.login, name='login'),
    path('logout/', view=account_view.logout, name='logout'),
    path('sign_up/', view=account_view.create_account, name="sign_up"),
    path('account/', view=account_view.account_details, name="account"),

    #test
    path('test/', view=views.test, name='test'),
    path('members/', views.memebers, name='members'),
]
