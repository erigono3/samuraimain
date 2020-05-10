from django import forms
from .models import Place , Placecomment

class Placeform(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

class Placecommentform(forms.ModelForm):
    class Meta:
        model = Placecomment
        fields = '__all__'