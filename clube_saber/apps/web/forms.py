from django import forms

from .models.contact import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['created_at', 'updated_at']
