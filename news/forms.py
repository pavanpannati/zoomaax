from django import forms
from .models import subscription_alert

class subscription_forms(forms.ModelForm):
    class Meta:
        model=subscription_alert
        fields='__all__'