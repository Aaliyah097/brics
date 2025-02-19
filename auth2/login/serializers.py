from rest_framework import serializers


class Login2faSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class Login2faConfirmSerializer(serializers.Serializer):
    nonce = serializers.CharField()


class TokensPairSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
