from django import forms
from .models import CONTACT
# from django.contrib.messages.views import SuccessMessageMixin

class ContactForm(forms.ModelForm):
    class Meta:
        model = CONTACT
        fields = ('name','email','message')