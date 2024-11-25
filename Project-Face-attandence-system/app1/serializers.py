from rest_framework import serializers
from .models import Attendance, Student
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'computer_number', 'email', 'phone_number', 'student_class', 'password', 'image', 'authorized']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        return super().create(validated_data)


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
    
class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)
    date = serializers.DateField(format="%b. %d, %Y")
    check_in_time = serializers.TimeField(format="%I:%M:%S %p")
    check_out_time = serializers.TimeField(format="%I:%M:%S %p")

    class Meta:
        model = Attendance
        fields = [
            'student_name',
            'course_name',
            'date',
            'check_in_time',
            'check_out_time',
            'stayed_time',
        ]

