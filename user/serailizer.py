from rest_framework import serializers
from .models import User,EmailOtp

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","is_active","email"]


class EmailOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmailOtp
        fields ='__all__'