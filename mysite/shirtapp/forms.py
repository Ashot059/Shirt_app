from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Feedback
from .models import Buyer


def validate_name(value):
    pattern = r'^[a-zA-Z -]+$'
    if not re.match(pattern, value):
        raise ValidationError("The name can only contain letters, '-' and spaces.")


def validate_phone_number(value):
    if not value.isdigit() or len(value) != 9:
        raise ValidationError("The phone number must consist of 9 digits.")


def validate_credit_card_number(value):
    if not value.isdigit() or len(value) != 16:
        raise ValidationError("The credit card number must be 16 digits.")


def validate_delivery_address(value):
    pattern = r'^[a-zA-Z0-9/ -]+$'
    if not re.match(pattern, value):
        raise ValidationError("The delivery address can only contain letters, numbers and the signs '/', '-'.")


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'email', 'address', 'shirt_size', 'credit_card_number', 'valid_date', 'cvv']

    name = forms.CharField(label='Name', max_length=20, validators=[validate_name])
    address = forms.CharField(label='Address', max_length=30, validators=[validate_delivery_address])
    credit_card_number = forms.CharField(label='Credit Card Number', max_length=16,
                                         validators=[validate_credit_card_number])
    valid_date = forms.CharField(label='Valid Date', max_length=4)
    cvv = forms.CharField(label='CVV', max_length=3)
