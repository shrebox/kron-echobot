from django.db import models

class NameForm(models.Model):
    input_text = forms.CharField(label='Enter String', max_length=200)