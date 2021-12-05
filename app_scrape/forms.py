from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


widgets_textinput = forms.TextInput(
    attrs={
        "class": "form-control",
    }
)

class TextForm(forms.Form):
    
    search = forms.CharField(label="品名", widget=widgets_textinput)


    
