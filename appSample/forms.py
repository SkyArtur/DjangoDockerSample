from django import forms
from .models import Person


class FormPerson(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'birth', 'photo')
