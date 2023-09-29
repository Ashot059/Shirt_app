from django import forms
from django.core.exceptions import ValidationError
import re


def validate_name(value):
    pattern = r'^[a-zA-Z -]+$'
    if not re.match(pattern, value):
        raise ValidationError("Имя может содержать только буквы, знаки '-' и пробелы.")


def validate_phone_number(value):
    if not value.isdigit() or len(value) != 9:
        raise ValidationError("Номер телефона должен состоять из 9 цифр.")


def validate_credit_card_number(value):
    if not value.isdigit() or len(value) != 16:
        raise ValidationError("Номер кредитной карты должен состоять из 16 цифр.")


def validate_delivery_address(value):
    pattern = r'^[a-zA-Z0-9/ -]+$'
    if not re.match(pattern, value):
        raise ValidationError("Адрес доставки может содержать только буквы, цифры и знаки '/', '-'.")


class BuyForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}), validators=[validate_name])
    phone_number = forms.CharField(label='Номер телефона', max_length=9, required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}),
                                   validators=[validate_phone_number])
    credit_card_number = forms.CharField(label='Номер кредитной карты', max_length=16, required=True,
                                         widget=forms.TextInput(attrs={'placeholder': 'Номер кредитной карты'}),
                                         validators=[validate_credit_card_number])
    delivery_address = forms.CharField(label='Адрес доставки', required=True,
                                       widget=forms.TextInput(attrs={'placeholder': 'Ваш адрес доставки'}),
                                       validators=[validate_delivery_address])
