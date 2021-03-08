from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegisterPhone, ValidateOTPForm, RegisterUser, LoginForm, PasswordResetForm
from accounts.models import User, PhoneOTP
from accounts.serializers import CreateUserSerializer
from .serializers import LoginUserSerializer
from django.contrib.auth import authenticate, login
import random
import requests
import os
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    return render(request, 'register/base.html', {})

def registerpages(request, reset):
    print(reset)
    form = RegisterPhone(request.POST or None, initial={'phone': ''})
    print(form)
    if request.method == "POST":
        phone_number = form.cleaned_data['phone']
        if phone_number:
            phone = str(phone_number)
            request.session['phone_number'] = phone
            user = User.objects.filter(phone__iexact=phone)
            if user.exists() and reset == '0':
                print(reset)
                messages.error(request, "User is already registered!")
                return redirect('register:register-phone', reset='0') 
            else:
                key = sent_otp(phone)
                if key:
                    print(key)
                    old = PhoneOTP.objects.filter(phone__iexact=phone)
                    if old.exists():
                        old = old.first()
                        if old.count > 10:
                            messages.warning(request, "OTP Limit exceeded")
                            return redirect('register:register-phone')
                        old.count = old.count + 1
                        old.otp = key
                        old.save()
                        messages.success(request, "OTP Sent Successfully")
                        return redirect('register:validate-otp', reset_to_password=0)
                    else:
                        PhoneOTP.objects.create(phone=phone, otp=key)
                        messages.success(request, "OTP Sent Successfully")
                        return redirect('register:validate-otp', reset_to_password='0')
                else:
                    messages.error(request, "Error While Sending OTP")
        else:
            messages.warning(request, "Please enter Phone Number ")
            # return redirect('register:register-phone')
    return render(request, 'register/register_phone.html', {'form': form, 'flag': reset})


def sent_otp(phone):
    if phone:
        key = random.randint(999, 9999)
        return key
    return False

def validateOTP(request, reset_to_password='1'):
    form = ValidateOTPForm(request.POST or None, initial={'phone': request.session['phone_number'] if request.session.get('phone_number', None) else None, 'otp': ''})
    if request.method == "POST":
        if form.is_valid():
            otp_sent = form.cleaned_data['otp']
            phone = form.cleaned_data['phone']

        if phone and otp_sent:
            old = PhoneOTP.objects.filter(phone__iexact=phone)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp) == str(otp_sent):
                    old.validated = True
                    old.save()
                    messages.success(request, "OTP validated successfully")
                    print(reset_to_password)
                    if reset_to_password != '0':
                        return redirect('register:register-user')
                    else:
                        return redirect('register:password-reset', phone=phone)
                else:
                    messages.warning(request, "Incorrect OTP")
                    return redirect( 'register:validate-otp')
            else:
                messages.error(request, "Please validate your phone number")
                return redirect('register:register-phone')
        else:
            messages.error(request, "Either Incorrect OTP or Phone Number")
    return render(request, 'register/validate_otp.html', { 'form': form, 'reset': reset_to_password })

def registerUser(request):
    form = RegisterUser(request.POST or None, initial={'phone': request.session['phone_number'] if request.session.get('phone_number', None) else None, 'password': '', 'name': ''})
    if request.method == "POST":
        phone = request.POST.get('phone', False)
        password = request.POST.get('password', False)
        name = request.POST.get('name', False)
        if phone and password:
            #already registered user
            user = User.objects.filter(phone__iexact=phone).exists()
            if user:
                messages.error(request, "User Already exists")
                request.session['phone_number'] = phone
            else:
                old = PhoneOTP.objects.filter(phone__iexact=phone)
                if old.exists():
                    old = old.first()
                    validated = old.validated
                    if old.validated:
                        temp_data = {
                            'phone': phone,
                            'password': password,
                            'name': name
                        }
                        serializer = CreateUserSerializer(data=temp_data)
                        serializer.is_valid(raise_exception=True)
                        user = serializer.save()
                        print(user)
                        old.delete()
                        messages.success(request, "Account Created Successfully")
                        return redirect('register:register-phone', reset='0')
                    else:
                        messages.success(request, "OTP not verified yet, Please Validate Your OTP")
                        request.session['phone_number'] = phone
                        return redirect('register:validate-otp')
                else:
                    messages.warning(request, "Please register your phone number.")
                    request.session['phone_number'] = phone
                    return redirect('register:register-phone')
        else:
            messages.error(request, "Phone and Password are not set")
            request.session['phone_number'] = phone
    return render(request, 'register/register_user.html', {'form': form})



def loginUser(request):
    form = LoginForm(request.POST or None)
    print(request.user)
    print(request.method)
    if request.method == "POST":
        print(form)
        phone = form.cleaned_data['phone']
        password = form.cleaned_data['password']
        user = None
        if phone and password:
            print(request.POST)
            print(User.objects.filter(phone__iexact=phone))
            if User.objects.filter(phone__iexact=phone).exists():
                user = authenticate(request, phone=phone, password=password)
                if user:
                    login(request, user)
            else:
                messages.error(request, "Invalid Phone Number, Please enter a correct phone number")
            if not user:
                messages.warning(request, "Phone number and password aren't matching")
        else:
            messages.error(request, "Phone number and password aren't found")
            return redirect('login')
    return render(request, "register/login.html", {'form': form})

def resetPassword(request):
    phoneform = RegisterPhone()
    passwordform = PasswordResetForm()
    return render(request, 'register/password_reset.html', {'phoneform': phoneform, 'passwordform': passwordform})

def passwordReset(request, phone):
    form = PasswordResetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print(password1, password2)
            if password1 and password2:
                if password1 == password2:
                    user = User.objects.filter(phone__iexact=phone)
                    if user.exists():
                        user = user.first()
                        print(dir(user))
                        user.set_password(password1)
                        user.save()
                        return redirect('register:homepage')
            else:
                messages.warning("passwords don't match")
            
    return render(request, 'register/password_reset.html', {'form': form, 'phone_number': phone})