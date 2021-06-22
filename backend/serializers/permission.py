from rest_framework import serializers
from user.models import Permission


class PermissionListSerializer(serializers.ModelSerializer):
    

    class Meta:
        fields = '__all__'
        model = Permission


class PermissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission


class PermissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission


class PermissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission


class PermissionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission