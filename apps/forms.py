from django import forms
from .models import Message


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['name' , 'email' , 'text']

class Subscription(forms.Form):
    subject = forms.CharField(max_length=128)

    message = forms.CharField()
