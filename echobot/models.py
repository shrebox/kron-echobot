from django import forms

class NameForm(forms.Form):
    data = forms.CharField(label='Enter String', max_length=100)