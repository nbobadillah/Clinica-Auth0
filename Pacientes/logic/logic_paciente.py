from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_paciente(form):
    paciente = form.save()
    paciente.save()
    return ()