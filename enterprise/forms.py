from django.forms import ModelForm
from enterprise.models import Enterprise
from django.utils.translation import gettext_lazy as _

class EnterpriseForm(ModelForm):
    class Meta:
        model = Enterprise
        fields = ('name', 'dni', 'address', 'commune')
        labels = {
            'name': _('Nombre'),
            'dni': _('Rut'),
            'address': _('Dirección'),
            'commune': _('Comuna'),
        }
        help_texts = {
            'name': _('Nombre de tu empresa.'),
            'dni': _('Rut de tu empresa'),
            'address': _('Dirección de la empresa'),
            'commune': _('Comuna donde esta la empresa'),
        }
        error_messages = {
            'name': {
                'max_length': _("nombre demasiado largo!!."),
            },
            'dni': {
                'max_length': _("Rut demasiado largo!!."),
            },
            'address': {
                'max_length': _("Direcion demasiada larga!!."),
            },
            'commune': {
                'max_length': _("Comuna demasiada larga!!."),
            }
        }
       
    
