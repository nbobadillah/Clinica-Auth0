from ..models import Resultado

def get_resultados():
    queryset = Resultado.objects.all()
    return (queryset)

def get_resultado(id):
    variable = Resultado.objects.raw("SELECT * FROM resultados_resultado WHERE id=%s" % id)[0]
    return (variable)

def create_resultado(form):
    paciente = form.save()
    paciente.save()
    return ()


