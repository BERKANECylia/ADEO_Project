# http://www.jeffreyteruel.com/article/42
 #student forms.py
from django import forms
#from .models import Student
#from .models import House
from django.forms import ModelChoiceField

class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    house = forms.ModelChoiceField(queryset=House.objects.all(), initial=0)
 
    class Meta:


        model = ProgramTable
        fields = [
             "ID_ANO","PRG","ANNE_SCOLAIRE","SITE"
        ]
