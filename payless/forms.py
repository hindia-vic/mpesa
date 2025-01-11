from django import forms

class PaymentForm(forms.Form):
    phone_number=forms.CharField(max_length=20,label='phone_number')
    amount=forms.IntegerField(min_value=1)