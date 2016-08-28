from django import forms
from .models import DiscountData

class DiscountEntryForm(forms.ModelForm):
    class Meta:
        model = DiscountData
        fields = ("couponType", "couponVal", "minimumAmt", "couponCode",)
