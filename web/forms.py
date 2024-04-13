from django import forms
from django.utils.translation import gettext_lazy as _
from . models import Contact,Email
from django.forms import widgets

class ContactForm(forms.ModelForm):
  
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "email": widgets.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "phone": widgets.NumberInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "subject": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            "message": widgets.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Message"}),

     
        }


class Emailform(forms.ModelForm):
   
    class Meta:
        model = Email
        exclude = ("timestamp",)
        widgets = {
            
            "email": widgets.EmailInput(attrs={"class": "form-control input-group-field newsletter-input", "placeholder": "Enter your email address..."}),
          
        }


