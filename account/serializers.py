import re
from django.contrib.auth import authenticate
from rest_framework import serializers

from account.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'fullname', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise serializers.ValidationError("لطفاً یک ایمیل معتبر وارد کنید.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد.")
        if not re.search(r'[A-Za-z]', value) or not re.search(r'\d', value):
            raise serializers.ValidationError("رمز عبور باید شامل حروف و اعداد باشد.")
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            fullname=validated_data.get('fullname', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")
#
#         if email and password:
#             user = authenticate(username=email, password=password)
#             if user is None:
#                 raise serializers.ValidationError("ایمیل یا رمز عبور اشتباه است.")
#             if not user.is_active:
#                 raise serializers.ValidationError("این حساب کاربری غیر فعال است.")
#         else:
#             raise serializers.ValidationError("هر دو فیلد ایمیل و رمز عبور الزامی هستند.")
#
#         data["user"] = user
#         return data
