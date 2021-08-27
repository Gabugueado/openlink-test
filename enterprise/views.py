from .models import Enterprise
from enterprise.forms import EnterpriseForm
from django.views.generic import CreateView, ListView

# Create your views here.

class RegistroEmpresa(CreateView):
    model = Enterprise
    template_name = "crear.html"
    form_class = EnterpriseForm
    success_url = '/thanks/'

class ListarEmpresa(ListView):
    model = Enterprise
    template_name = "listar.html"