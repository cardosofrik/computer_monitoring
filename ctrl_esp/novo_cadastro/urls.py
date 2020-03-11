from django.urls import path
from novo_cadastro import views as standard

urlpatterns = [
    path('registro/',standard.register,name ='registro'),
    path('',standard.loginUser,name ='login'),
    path('logout/',standard.logoutUser,name = "logout"),


]

