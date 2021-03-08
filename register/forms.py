from django import forms
from accounts.models import User


class RegisterPhone(forms.Form):
    phone = forms.IntegerField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password"}))

class ValidateOTPForm(forms.Form):
    phone = forms.CharField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password"}))
    otp = forms.IntegerField(label = 'OTP', widget=forms.TextInput(attrs={'class': "form-control password"}))


class RegisterUser(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100 , widget=forms.TextInput(attrs={'class': "form-control password"}))
    phone = forms.CharField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ( 'name','phone', 'password')



class LoginForm(forms.Form):
    phone = forms.CharField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))