from django import forms

class NameForm(forms.Form):
    celeb_name = forms.CharField(label='Celebrity name', max_length=100)