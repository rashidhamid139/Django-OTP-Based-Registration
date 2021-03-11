from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class RegisterPhone(forms.Form):
    phone = forms.IntegerField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password input-width"}))

class ValidateOTPForm(forms.Form):
    phone = forms.CharField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password input-width"}))
    otp = forms.IntegerField(label = 'OTP', widget=forms.TextInput(attrs={'class': "form-control password input-width-otp"}))


class RegisterUser(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100 , widget=forms.TextInput(attrs={'class': "form-control password input-width"}))
    phone = forms.CharField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password input-width"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control input-width"}))

    class Meta:
        model = User
        fields = ( 'name','phone', 'password')



class LoginForm(forms.Form):
    phone = forms.CharField(label = 'Phone Number', widget=forms.TextInput(attrs={'class': "form-control password input-width"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control input-width"}))


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control input-width"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': "form-control input-width"}))




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
