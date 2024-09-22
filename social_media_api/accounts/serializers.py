from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the User model
User = get_user_model()

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Using CharField to handle password input
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    # Validate that the password and password confirmation match
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    # Create a new user and generate a token for them
    def create(self, validated_data):
        # Remove password_confirm from validated data as we don't need to save it
        validated_data.pop('password_confirm')

        # Create a new user with the provided data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create a token for the new user
        Token.objects.create(user=user)

        return user
