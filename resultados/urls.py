from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('resultados/', views.resultado_list, name='resultadoList'),
    path('resultado/<id>', views.single_resultado, name='singleResultado'),
    path('resultadocreate/', csrf_exempt(views.resultado_create), name='resultadoCreate'),
]
