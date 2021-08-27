from django.urls import path
from enterprise.views import RegistroEmpresa, ListarEmpresa

urlpatterns = [
    path('registrar', RegistroEmpresa.as_view(), name='registrar_empresa'),
    path('listar', ListarEmpresa.as_view(), name='listar_empresa')
]