from django import forms
from .models import Foo
class PathForm(forms.ModelForm):
    class Meta:
        model=Foo
