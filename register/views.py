from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . forms import RegisterPhone, ValidateOTPForm, RegisterUser, LoginForm, PasswordResetForm
from .models import User, PhoneOTP
from .serializers import CreateUserSerializer
from .serializers import LoginUserSerializer
from django.contrib.auth import authenticate, login
import random
import requests
import os
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(request):
    return render(request, 'register/base.html', {})

def registerpages(request):
    if request.user.is_authenticated:
        return redirect('register:homepage')
    form = RegisterPhone(request.POST or None)
    if request.method == "POST":
        print(form)
        phone_number = form.cleaned_data['phone']
        if phone_number:
            phone = str(phone_number)
            request.session['phone_number'] = phone
            user = User.objects.filter(phone__iexact=phone)
            if user.exists():
                messages.error(request, "User is already registered!, Please proceed to user registration page." )
                return redirect('register:register-phone' ) 
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
                        return redirect('register:validate-otp')
                    else:
                        PhoneOTP.objects.create(phone=phone, otp=key)
                        messages.success(request, "OTP Sent Successfully")
                        return redirect('register:validate-otp' )
                else:
                    messages.error(request, "Error While Sending OTP")
        else:
            messages.warning(request, "Please enter Phone Number ")
            # return redirect('register:register-phone')
    return render(request, 'register/register_phone.html', {'form': form })


def sent_otp(phone):
    if phone:
        key = random.randint(999, 9999)
        return key
    return False

def validateOTP(request ):
    if request.user.is_authenticated:
        return redirect('register:homepage')
    print("Old")
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
                    return redirect('register:register-user')
                else:
                    messages.warning(request, "Incorrect OTP")
                    return redirect( 'register:validate-otp')
            else:
                messages.error(request, "Please validate your phone number")
                return redirect('register:register-phone')
        else:
            messages.error(request, "Either Incorrect OTP or Phone Number")
    return render(request, 'register/validate_otp.html', { 'form': form, })

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('register:homepage')
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
                        return redirect('login' )
                    else:
                        messages.success(request, "OTP not verified yet, Please Validate Your OTP")
                        request.session['phone_number'] = phone
                        return redirect('register:validate-otp')
                else:
                    messages.warning(request, "Please register your phone number.")
                    request.session['phone_number'] = phone
                    print(request.session['phone_number'])
                    return redirect('register:register-phone')
        else:
            messages.error(request, "Phone and Password are not set")
            request.session['phone_number'] = phone
    return render(request, 'register/register_user.html', {'form': form})



def loginUser(request):
    if request.user.is_authenticated:
        return redirect('register:homepage')
    form = LoginForm(request.POST or None)
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
                    return redirect('register:homepage')
            else:
                messages.error(request, "Invalid Phone Number, Please enter a correct phone number")
            if not user:
                messages.error(request, "Phone number and password aren't matching")
        else:
            messages.error(request, "Phone number and password aren't found")
            return redirect('login')
    return render(request, "register/login.html", {'form': form})

def resetPassword(request):
    phoneform = RegisterPhone()
    passwordform = PasswordResetForm()
    return render(request, 'register/password_reset.html', {'phoneform': phoneform, 'passwordform': passwordform})

def passwordReset(request):
    form = PasswordResetForm(request.POST or None)
    phone = request.session.get('phone_number', None)
    if phone is None:
        return redirect('register:ajax-reset-password')
    print(request.session.get('phone_number', 'no session found'), "checking session")
    if request.method == "POST":
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print(password1, password2)
            del request.session['phone_number']
            if password1 and password2:
                if password1 == password2:
                    user = User.objects.filter(phone__iexact=phone)
                    if user.exists():
                        user = user.first()
                        user.set_password(password1)
                        user.save()
                        return redirect('login')
            else:
                messages.error("passwords don't match")
            
    return render(request, 'register/password_reset.html', {'form': form, 'phone_number': phone})


def resetPasswordAjax(request):
    if request.is_ajax():
        print(request.POST)
        phone = request.POST.get('phone_number', '')
        otp = request.POST.get('otp_number', '')
        if phone:
            if not otp:
                user = User.objects.filter(phone__iexact=phone)
                print(user)
                if user.exists():
                    old = PhoneOTP.objects.filter(phone__iexact=phone)
                    print(old)
                    key = sent_otp(phone)
                    if old.exists():
                        old = old.first()
                        print(old)
                        if key:
                            print(key)
                            old.count = old.count + 1
                            old.otp = key
                            old.save()
                            return JsonResponse({
                                'status': True,
                                'details': "OTP sent successfully",
                                'case': 'validate',
                                "url": ''
                            }) 
                    else:
                        new = PhoneOTP.objects.create(phone=phone, otp=key)
                        new.validated = True
                        new.save()
                        print(key)
                        print("---")
                        return JsonResponse({
                                    'status': True,
                                    'details': "OTP sent successfully",
                                    'case': 'validate',
                                    "url": ''
                                })          
                else:
                    return JsonResponse({
                        'status': False,
                        'details': "User doen't exists, Please register",
                        'case': 'register',
                        'url': reverse('register:register-phone' )
                    }, status=200)
            elif otp:
                old = PhoneOTP.objects.filter(phone__iexact=phone)
                print("old", old.exists())
                if old.exists():
                    old = old.first()
                    old_otp = old.otp
                    if str(old_otp) == str(otp):
                        old.validated = True
                        old.save()
                        request.session['phone_number'] = phone
                        return JsonResponse({
                            'status': True,
                            'details': "OTP validated Successfully",
                            "case": "validate",
                            "url": reverse('register:password-reset' )
                        })
                    else:
                        return JsonResponse({
                            'status': False,
                            'details': "Incorrect OTP",
                            "case": "validate",
                            "url": ""
                        })
    
    return render(request, 'register/resetpasswordAjax.html', {'form': 'form' })

def validatePasswordResetOTP(request):
    if request.is_ajax():
        return JsonResponse({}, status=200)