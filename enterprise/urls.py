from django.urls import path
from enterprise.views import RegistroEmpresa

urlpatterns = [
    path('registrar', RegistroEmpresa.as_view(), name='registrar_empresa'),
]