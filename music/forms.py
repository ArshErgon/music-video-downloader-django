from django import forms


class MusicUrl(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'paste and hit enter'}))
