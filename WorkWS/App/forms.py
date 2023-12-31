from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField(required=False)
#     email = forms.EmailField(required=False)

# class UserForm(forms.Form):
#     name = forms.CharField(min_length=2, max_lenght=20)
#     email = forms.EmailField(required=False)

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField(min_value=1, max_value=100)
    weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()