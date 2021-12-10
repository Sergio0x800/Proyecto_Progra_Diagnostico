from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import Diagnosticos

# from diagnosticos.models import Diagnosticos


# Utilities
from datetime import datetime

# Create your views here.
def main(request):
  diagnosticosListados = Diagnosticos.objects.all()
  return render(request, 'diagnosticos/createDiagnostico.html', {"diagnosticos": diagnosticosListados})

def editDiagnostico(request, Id):
  diagnostico = Diagnosticos.objects.get(IdDiagnostico=Id)
  return render(request, 'diagnosticos/editDiagnostico.html', {"diagnostico": diagnostico})

def editDiagnosticoSet(request):
  IdDiagnostico = request.POST['IdDiagnostico']
  diagnostico = Diagnosticos.objects.get(IdDiagnostico = IdDiagnostico)
  diagnostico.Placa = request.POST['placa']
  diagnostico.Cliente = request.POST['cliente']
  diagnostico.Fecha = request.POST['fecha']
  diagnostico.Tipo = request.POST['tipo']
  diagnostico.Estado = request.POST['estado']
  diagnostico.save()
  return redirect('diagnosticos')

def eliminarDiagnostico(request, Id):
  diagnostico = Diagnosticos.objects.get(IdDiagnostico=Id)
  diagnostico.delete()
  return redirect('diagnosticos')

def iniciarDiagnostico(request, Id):
  diagnostico = Diagnosticos.objects.get(IdDiagnostico=Id)
  return render(request, 'diagnosticos/iniciarDiagnostico.html', {"diagnostico": diagnostico})
  #return redirect('detalleDiagnostico', IdDiagnostico=Id)

def finalizarDiagnostico(request, Id):
  diagnostico = Diagnosticos.objects.get(IdDiagnostico=Id)
  diagnostico.Estado = 'Finalizado'
  diagnostico.save()
  return redirect('diagnosticos')
  