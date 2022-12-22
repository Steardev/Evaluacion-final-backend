from django.shortcuts import render, redirect
from .serializers import InscritoSerializer, InstitucionSerializer
from .forms import FormInscrito
from .models import Inscrito, Institucion
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

#crud completo#

def crud(request):
    return render(request, 'listar_inscripciones.html', {})

def lista_inscrito(request):
    inscri = Inscrito.objects.all()
    data = {'inscrito': inscri}
    return render(request, 'listar_inscripciones.html', data)

def agregar_inscrito(request):
    form = FormInscrito()
    if request.method == 'POST':
        form = FormInscrito(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_inscripcion.html', data)

def eliminar_inscrito(request, id):
    inscri = Inscrito.objects.get(id = id)
    inscri.delete()
    return redirect('/listado_inscrito')

def actualizar_inscrito(request, id):
    inscrito_actualizado = Inscrito.objects.get(id = id)
    form = FormInscrito(instance=inscrito_actualizado)
    if request.method == 'POST':
        form = FormInscrito(request.POST, instance=inscrito_actualizado)
        if form.is_valid() :
            form.save()
        return redirect('/listado_inscrito')
    data = {'form' : form}
    return render(request, 'agregar_inscripcion.html', data)



def verAPI(request):
    inscri = Inscrito.objects.all()
    insti = Institucion.objects.all()
    data = {'institucion' : list(insti.values('institucion'))}
    data.update ({'inscrito': list(inscri.values('nombre','telefono','fechaInscripcion','institucion','horaInscripcion','estado','observacion'))})
    return JsonResponse(data)

# class based view#

class InscritosLista(APIView):
    def get(self, request):
        inscri = Inscrito.objects.all()
        serial = InscritoSerializer(inscri, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritoSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritosDetalle(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(id=pk)
        except Inscrito.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscritoSerializer(inscri)
        return Response(serial.data)
                
    def put(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscritoSerializer(inscri, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        inscri = self.get_object(pk)
        inscri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #function based view de intituciones#
    
    
@api_view (['GET', 'POST'])
def InstitucionesLista(request):
    if request.method == 'GET':
        insti = Institucion.objects.all()
        serial = InstitucionSerializer(insti, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data= request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def InstitucionesDetalle(request, pk):
    try:
        insti = Institucion.objects.get(id=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(insti)
        return Response(serial.data)
        
    if request.method == 'PUT':
        serial = InstitucionSerializer(insti, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        insti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    