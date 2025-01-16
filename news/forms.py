from django import forms
from .models import subscription_alert

class subscription_forms(forms.ModelForm):
    class Meta:
        model=subscription_alert
        fields=['First_name',"Last_name",'Email']
    
        widgets={
                'First_name':forms.TextInput(attrs={
                    'placeholder':'First Name',
                    'class':'form_control'
                }),
                'Email':forms.EmailInput(attrs={
                    'class':'form-control',
                    'placeholder':'zoomaax@gmail.com',
                }),
                'Last_name':forms.TextInput(attrs={
                    'placeholder':'Last Name',
                    'class':'form_control'
                }),
        }