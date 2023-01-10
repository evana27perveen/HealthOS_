from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'phone_number', 'is_subscribed', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'is_subscribed': {'read_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, validated_data):
        user = CustomUser.objects.get(id=validated_data['id'])
        user.is_subscribed = True
        user.save()
        return user

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'primary_phone_number': {'read_only': True}}
