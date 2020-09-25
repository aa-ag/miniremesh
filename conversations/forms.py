from django import forms
from django.forms import ModelForm, Textarea
from .models import Conversation, Message, Thought

class CreateConversation(ModelForm):
    class Meta:
        model = Conversation
        fields = ['title']

class CreateMessage(ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={"class": "form-control"})
        }

class CreateThought(ModelForm):
    class Meta:
        model = Thought
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={"class": "form-control"})
        }