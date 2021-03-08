from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'phone', 'password' )
        extra_kwargs ={"password": { "write_only": True}}


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user = User.objects.create(name=validated_data['name'], phone=validated_data['phone'])
        user.set_password(validated_data['password'])
        print(validated_data)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'phone', 'first_login')

class LoginUserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type': 'password'}, trim_whitespace = False
    )
    def validate(self, data):
        print(self.data)
        phone = self.data.get('phone')
        password = self.data.get('password')
        print(phone + "444" + password)
        if phone and password:
            if User.objects.filter(phone=phone).exists():
                print(phone, password)
                user = authenticate(request = self.context.get('request'), phone=phone, password=password)
                print(user)
            else:
                msg = {
                    'detail': 'Phone number not found',
                    'status': False
                }
                raise serializers.ValidationError(msg)
            if not user:
                msg = {
                    'detail': "Phone number and password aren't matching",
                    'status': False
                }
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = {
                'detail': 'Phone number and password not found',
                'status': False
            }
            raise serializers.ValidationError(msg, code='authorixation failed')
        
        data['user'] = user
        return data