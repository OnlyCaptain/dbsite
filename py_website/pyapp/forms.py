from django import forms
# from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='用户', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='密码  ', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='密码  ', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
