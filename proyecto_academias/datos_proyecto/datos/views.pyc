# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse

from django.template import RequestContext
from django.db.models import *
from datos.models import *
import json
from datos.forms import *

def inicio(request):
    return render(request, 'index.html')

def defunciones_fetales(request):
    """
    """
    context = {'anio_def': None, 'sexo': None, 'sem_gestac': None, 'edad': None, 'hijos_vivos': None,
    'hijos_nac_vivos': None, 'hijos_nac_muertos': None, 'estado_civil': None, 'etnia': None}

    if request.method=='POST':
        formulario = formularioDefuncionesFetales(request.POST)
        valorselectGrupo = formulario['selectanio_def'].value()
        valorselectEspecie = formulario['sexo'].value()
        valorselectEspecie = formulario['sem_gestac'].value()
        valorselectEspecie = formulario['edad'].value()
        valorselectEspecie = formulario['hijos_vivos'].value()
        valorselectEspecie = formulario['hijos_nac_vivos'].value()
        valorselectEspecie = formulario['hijos_nac_muertos'].value()
        valorselectEspecie = formulario['estado_civil'].value()
        valorselectEspecie = formulario['etnia'].value()
    else:
        formulario = formularioDefuncionesFetales()

    context['formulario'] = formulario

    return render(request, 'defunciones_fetales.html', context, context_instance=RequestContext(request))



def localizacion(request):
    context = {'selectGrupo': None, 'selectEspecie': None, 'selectRegion': None, 'selectProvincia': None, 'selectYear': None}

    if request.method=='POST':
        formulario = formularioAsideLocalizacion(request.POST)
        valorselectGrupo = formulario['selectGrupo'].value()
        valorselectEspecie = formulario['selectEspecie'].value() 
    else:
        formulario = formularioAsideLocalizacion()
        especie = Especie.objects.filter(especie='Pollitos Pollitas Pollos Pollas').distinct()
        localizacion=Localizacion.objects.filter(region='REGIÓN COSTA')
    context['formulario'] = formulario
    context['especie'] = especie
    context['localizacion'] = localizacion
    return render(request, 'localizacion.html', context, context_instance=RequestContext(request))



def estratos(request):
    """
    """
    context = {'selectGrupo': None, 'selectEspecie': None, 'selectRegion': None, 'selectProvincia': None, 'selectYear': None}

    if request.method=='POST':
        formulario = formularioAside(request.POST)
        valorselectGrupo = formulario['selectGrupo'].value()
        valorselectEspecie = formulario['selectEspecie'].value() 
    else:
        formulario = formularioAside()
        datos = [{
            'name': 'John',
            'data': [5, 3, 4, 7, 2]
        }, {
            'name': 'Rene',
            'data': [2, 2, 3, 2, 1]
        }, {
            'name': 'Joe',
            'data': [3, 4, 4, 2, 5]
        }]
    datos1 = json.dumps(datos) 
    print datos1
    context['formulario'] = formulario
    context['datos'] = datos1
    return render(request, 'estratos.html', context, context_instance=RequestContext(request))
    ##return render(request, 'estratos.html')



def derivados(request):
    """
    """
    context = {'selectGrupo': None, 'selectEspecie': None, 'selectRegion': None, 'selectProvincia': None, 'selectYear': None}

    if request.method=='POST':
        formulario = formularioAside(request.POST)
        valorselectGrupo = formulario['selectGrupo'].value()
        valorselectEspecie = formulario['selectEspecie'].value() 
    else:
        formulario = formularioAside()
    context['formulario'] = formulario
    return render(request, 'derivados.html', context, context_instance=RequestContext(request))
    ##return render(request, 'derivados.html')


#Funcion para cargar las especies segun el grupo
@csrf_exempt
def funcion_Ajax_Especies(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        grupo = request.POST.getlist('valor')[0]
        especiesseleccionadas = serializers.serialize('json', Especie.objects.filter(grupo__startswith = grupo ))
        req['especiesseleccionadas'] = especiesseleccionadas
        req['mensaje'] = 'Correcto .... cargando datos '
        return JsonResponse(req, safe=False)