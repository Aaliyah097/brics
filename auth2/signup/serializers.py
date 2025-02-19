from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SignupConfirmSerializer(serializers.Serializer):
    nonce = serializers.CharField()
    password = serializers.CharField()
