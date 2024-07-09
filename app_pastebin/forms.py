from django import forms
from .models import Paste


class CreatePasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ('title', 'content')
