
from django.forms import forms,ModelForm
from django import forms
from django.contrib.auth.models import User

from .models import booktbl,genretbl



class mangaaddform(ModelForm):
    class Meta:
        model = booktbl
        fields = '__all__'

    
      


class genreaddform(ModelForm):
    class Meta:
        model = genretbl
        fields = '__all__'
    



