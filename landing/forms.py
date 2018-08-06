from django import forms
from .models import *

class GamersForm (forms.ModelForm):

    class Meta:
        model = Gamer
        exclude = [""]