from django import forms
from .models import Order

"""
	Payments Form - contains cc ccv, expiry and hidden stripe id
"""


class MakePaymentForm(forms.Form):

	# time choices
    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]

    credit_card_number = forms.CharField(
        label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


"""
	The Order Form with necessary fields
"""


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode',
                  'town_or_city', 'street_address1', 'street_address2', 'county')
