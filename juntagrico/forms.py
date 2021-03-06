# -*- coding: utf-8 -*-
from django.forms import CharField, PasswordInput, Form, ValidationError, ModelForm, TextInput, CheckboxInput, DateInput

from juntagrico.models import Member, Subscription


class PasswordForm(Form):
    password = CharField(label='Passwort', min_length=4, widget=PasswordInput())
    passwordRepeat = CharField(label='Passwort (wiederholen)', min_length=4, widget=PasswordInput())

    def clean_password_repeat(self):
        if self.data['password'] != self.data['passwordRepeat']:
            raise ValidationError('Passwörter stimmen nicht überein')
        return self.data['passwordRepeat']


class MemberProfileForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email',
                  'addr_street', 'addr_zipcode', 'addr_location',
                  'birthday', 'phone', 'mobile_phone', 'reachable_by_email']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Berta', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Muster', 'class': 'form-control'}),
            'addr_street': TextInput(attrs={'placeholder': 'Zürcherstrasse 123', 'class': 'form-control'}),
            'addr_zipcode': TextInput(attrs={'placeholder': '8000', 'class': 'form-control'}),
            'addr_location': TextInput(attrs={'placeholder': 'Zürich', 'class': 'form-control'}),
            'birthday': TextInput(attrs={'placeholder': '01.12.1956', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': '044 123 45 67', 'class': 'form-control'}),
            'mobile_phone': TextInput(attrs={'placeholder': '076 123 45 67', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'beate@muster.ch', 'class': 'form-control'}),
            'reachable_by_email': CheckboxInput(attrs={'class': 'onoffswitch'}),
        }


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = ['start_date']
        widgets = {
            'start_date': DateInput(attrs={'format': '%d.%m.%y', 'class': 'form-control'}),
        }


class RegisterMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email',
                  'addr_street', 'addr_zipcode', 'addr_location',
                  'birthday', 'phone', 'mobile_phone']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Berta', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Muster', 'class': 'form-control'}),
            'addr_street': TextInput(attrs={'placeholder': 'Zürcherstrasse 123', 'class': 'form-control'}),
            'addr_zipcode': TextInput(attrs={'placeholder': '8000', 'class': 'col-xs-2'}),
            'addr_location': TextInput(attrs={'placeholder': 'Zürich', 'class': 'form-control'}),
            'birthday': TextInput(attrs={'placeholder': '01.12.1956', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': '044 123 45 67', 'class': 'form-control'}),
            'mobile_phone': TextInput(attrs={'placeholder': '076 123 45 67', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'beate@muster.ch', 'class': 'form-control'})
        }
