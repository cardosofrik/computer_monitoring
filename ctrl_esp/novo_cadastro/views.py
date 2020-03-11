from django.shortcuts import render,redirect,render_to_response
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        print(username)
        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            messages.info(request, " Usuario em uso")
            return redirect('registro')
        else:
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request, newUser)
            messages.info(request, " Usuario cadastrado")
            return redirect("login")


    context = {
        "form": form
    }
    #return redirect()
    return render(request, "registro.html",context)




def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.warning(request, " Verifique usuario/senha")
            return render(request, "login.html", context)


        print("========================================:::>sucesso")
        login(request, user)
        return redirect("dashboard")
    return render(request, "login.html", context)



def logoutUser(request):
    logout(request)
    messages.success(request, " Até mais...")
    return redirect("login")



def erro403(request):
    return render(request,"403.html")

def erro404(request):
    return render(request, "404.html")

def erro500(request):
    return render(request, "500.html")

