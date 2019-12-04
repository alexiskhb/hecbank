from django import forms


class PaymentForm(forms.Form):
    receiver = forms.CharField(max_length=100)
    amount = forms.IntegerField(widget=forms.NumberInput())
