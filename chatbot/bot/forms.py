from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    post=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'input',
            'placeholder':'Write message'
        }
    ))

    class Meta:
        model=Message
        fields=('post',)