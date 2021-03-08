from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class LoginForm(forms.Form):
    phone = forms.IntegerField(label = 'Phone Number')
    password = forms.CharField(widget=forms.PasswordInput)

class VerifyForm(forms.Form):
    key = forms.IntegerField(label = 'Please Enter OTP here')

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone', )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        qs = User.objects.filter(phone=phone)
        if qs.exists():
            raise forms.ValidationError("Phone is already registered")
        return phone

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password's don't match")
        return password2

class TempRegisterForm(forms.Form):
    phone = forms.IntegerField()
    otp = forms.IntegerField()


class SetPasswordForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone', )


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password's don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ( 'phone', 'name', 'active', 'admin')

    def clean_password(self):
        return self.initial['password']