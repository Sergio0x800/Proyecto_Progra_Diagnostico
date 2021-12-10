from django.shortcuts import render

# Create your views here.
def detalleDiagnostico(request):
  diagnosticosListados = Diagnosticos.objects.all()
  return render(request, 'diagnosticos/createDiagnostico.html', {"diagnosticos": diagnosticosListados})