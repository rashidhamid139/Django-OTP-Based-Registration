from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, PhoneOTP
from .serializers import CreateUserSerializer, LoginSerializer
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from rest_framework import permissions
from django.contrib.auth import login

import requests
import random
import os

# Create your views here.
class ValidatePhoneSendOTP(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone')
        print(phone_number)
        if phone_number:
            phone = str(phone_number)
            user = User.objects.filter(phone__iexact=phone)
            if user.exists():
                return Response({
                    'status': False,
                    'details': 'Phone number already registered'
                })
            else:
                key = sent_otp(phone)
                if key:
                    old = PhoneOTP.objects.filter(phone__iexact=phone)
                    if old.exists():
                        old  = old.first()
                        if old.count > 10:
                            return Response({
                                'status': False,
                                'details': "OTP Limit exceeded."
                            })
                        old.count = old.count + 1
                        old.save()
                        print("count increased: ", old.count)
                        return Response({
                            'status': True,
                            'details': 'OTP sent successfully'
                        })
                    else:
                        PhoneOTP.objects.create(phone=phone, otp=key )
                        print(key)
                        return Response({
                            'status': True,
                            'details': 'OTP sent successfully'
                        })
                else:
                    return Response({
                        'status': False,
                        'details': 'Error While sending OTP'
                    })
        else:
            return Response({
                'status': False,
                'details': 'Phone number is not given in the Post request'
            })



def sent_otp(phone):
    if phone:
        key = random.randint(999, 9999)
        return key
    else:
        return False

class ValidateOTP(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        otp_sent = request.data.get('otp', False)

        if phone and otp_sent:
            old = PhoneOTP.objects.filter(phone__iexact=phone)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp) == str(otp_sent):
                    old.validated = True
                    old.save()
                    return Response({
                        'status': True,
                        'details': 'OTP validated Successfully'
                    })
                else:
                    return Response({
                        'status': False,
                        'details': 'OTP Incorrect'
                    })
            else:
                return Response({
                    'status': False,
                    'details': 'Please validate your phone number first'
                })
        else:
            return Response({
                        'status': False,
                        'details': 'Please provide both phone and otp'
                    })

class Register(APIView):

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        password = request.data.get('password', False)

        if phone and password:
            old = PhoneOTP.objects.filter(phone__iexact=phone)
            if old.exists():
                old = old.first()
                validated = old.validated
                if validated:
                    temp_data = {
                        'phone': phone,
                        'password': password
                    }
                    serailzer = CreateUserSerializer(data = temp_data)
                    serailzer.is_valid(raise_exception=True)
                    user = serailzer.save()
                    old.delete()
                    return Response({
                        'status': True,
                        'details': 'Account created successfully'
                    })
                else:
                    return Response({
                        'status': False,
                        'details': 'OTP not verified yet, Please validate OTP first'
                    })
            else:
                return Response({
                    'status': False,
                    'details': 'Please Verfiy phone first'
                })
        else:
            return Response({
                'status': False,
                'details': 'Phone and Password are not set'
            })

class LoginAPI(KnoxLoginView):
    permission_classes = ( permissions.AllowAny, )

    def post(self, request, format=None):
        serailizer = LoginSerializer(data = request.data )
        print(serailizer)
        serailizer.is_valid(raise_exception=True)
        print(serailizer.validated_data)
        user = serailizer.validated_data['user']
        login(request, user)
        return super().post(request, format=None)