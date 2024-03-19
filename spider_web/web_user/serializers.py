from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'date_of_birth', 'country', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        # Remove 'confirm_password' if it exists in validated_data
        confirm_password = validated_data.pop('confirm_password', None)
        
        # Create the user without 'confirm_password'
        user = CustomUser.objects.create_user(**validated_data)
        
        return user
