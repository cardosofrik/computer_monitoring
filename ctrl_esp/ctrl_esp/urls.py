from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from novo_cadastro import views as standardPageErro

from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dispositivo.urls')),
    path('', include('novo_cadastro.urls')),
    path('403/', standardPageErro.erro403, name="403"),
    path('404/', standardPageErro.erro404, name="404"),
    path('500/', standardPageErro.erro500, name="500"),

]



urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)