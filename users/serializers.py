from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()  # Временно уберем EmailField
    password = serializers.CharField()

    def validate_email(self, value):
        print(f"validate_email: {value}")
        return value

    def validate_password(self, value):
        print(f"validate_password: {value}")
        return value

    def validate(self, attrs):
        print("=== VALIDATE METHOD CALLED ===")
        email = attrs.get('email')
        password = attrs.get('password')

        print(f"Final - Email: {email}, Password: {password}")

        if email and password:
            try:
                user = User.objects.get(email=email)
                print(f"User found: {user.email}")
                
                # Простая проверка пароля
                if user.check_password(password):
                    print("PASSWORD CORRECT!")
                    attrs['user'] = user
                    return attrs
                else:
                    print("PASSWORD INCORRECT!")
                    raise serializers.ValidationError('Invalid credentials')
                    
            except User.DoesNotExist:
                print("User not found")
                raise serializers.ValidationError('Invalid credentials')

        raise serializers.ValidationError('Email and password are required')