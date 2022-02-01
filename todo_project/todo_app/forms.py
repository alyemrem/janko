from django import forms
from django.db.models import fields
from .models import Todos

class ListForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title", "description", "finished", "date"]
        


