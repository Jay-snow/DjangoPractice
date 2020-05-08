from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(label="UserName", max_length=100)
    password = forms.CharField(label="Password", max_length=12, widget=forms.PasswordInput)