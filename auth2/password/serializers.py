from rest_framework import serializers


class PasswordChangeSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordChangeConfirmSerializer(serializers.Serializer):
    nonce = serializers.CharField()
    new_password = serializers.CharField()
