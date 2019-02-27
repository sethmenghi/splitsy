from django import forms

from .models import Receipt


class ReceiptCreation(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ('image',)
