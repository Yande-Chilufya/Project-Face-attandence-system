from rest_framework import serializers
from .models import Student
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'computer_number', 'email', 'phone_number', 'student_class', 'image', 'authorized']


class SignInSerializer(serializers.Serializer):
    computer_number = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        computer_number = data.get('computer_number')
        password = data.get('password')

        user = authenticate(username=computer_number, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid computer number or password.")

        refresh = RefreshToken.for_user(user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
