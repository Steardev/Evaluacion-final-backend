"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seminarioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.index),
    path('listado_inscrito/', views.lista_inscrito),
    path('agregar_inscrito/', views.agregar_inscrito),
    path('eliminar_inscrito/<int:id>/', views.eliminar_inscrito),
    path('actualizar_inscrito/<int:id>/', views.actualizar_inscrito),
    path('api/', views.verAPI),
    path('inscritos/', views.InscritosLista.as_view()),
    path('inscrito/<int:pk>', views.InscritosDetalle.as_view()),
    path('instituciones/', views.InstitucionesLista),
    path('instituciones/<int:pk>', views.InstitucionesDetalle),
]
