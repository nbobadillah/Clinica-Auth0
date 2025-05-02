from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import ResultadoForm
from .logic.resultado_logic import get_resultado, get_resultados, create_resultado
from django.contrib.auth.decorators import login_required
# Descomentar cuando se cree el archivo monitoring/auth0backend.py
#from monitoring.auth0backend import getRole

@login_required
def resultado_list(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        resultados = get_resultados()
        context = {
            'resultado_list': resultados
        }
        return render(request, 'Variable/variables.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_resultado(request, id=0):
    resultado = get_resultado(id)
    context = {
        'resultado': resultado
    }
    return render(request, 'Resultado/resultado.html', context)

@login_required
def resultado_create(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        if request.method == 'POST':
            form = ResultadoForm(request.POST)
            if form.is_valid():
                create_resultado(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created resultado')
                return HttpResponseRedirect(reverse('resultadoCreate'))
            else:
                print(form.errors)
        else:
            form = ResultadoForm()

        context = {
            'form': form,
        }
        return render(request, 'Resultado/resultadoCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
