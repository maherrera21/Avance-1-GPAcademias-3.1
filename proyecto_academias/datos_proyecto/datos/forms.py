#encoding:utf-8 
from django import forms
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

from datos.models import *

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import uuid
from django.contrib.auth.hashers import check_password


class Defunciones_Fetales(forms.Form):

    anio_def = forms.ChoiceField([(y, y) for y in DefunFetal.objects.values('anio_def').distinct().order_by("anio_def")])
    sexo = forms.ChoiceField([(y, y) for y in DefunFetal.objects.values('sexo').distinct().order_by("sexo")]