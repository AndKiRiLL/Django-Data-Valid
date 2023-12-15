from django import forms

class InputEmail(forms.Form):
    email = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'email', 'placeholder': 'ivanov_ivan@mail.ru'}))

class InputPassword(forms.Form):
    password = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__input', 'name': 'password', 'placeholder': '***********'}))

class InputName(forms.Form):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form__block__title__input__top form__block__input', 'name': 'name', 'placeholder': 'Иван'}))
