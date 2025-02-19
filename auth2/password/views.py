from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from auth2.password.serializers import PasswordChangeSerializer, PasswordChangeConfirmSerializer
from users.get_user_by_email import get_user_by_email
from auth2.nonce.create_nonce import create_nonce
from auth2.password.send_change_email import send_change_email
from auth2.nonce.get_email_by_nonce import get_email_by_nonce


@extend_schema(
    summary="Смена пароля",
    request=PasswordChangeSerializer
)
@api_view(['POST'])
def password_change(request):
    serializer = PasswordChangeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    
    user = get_user_by_email(serializer.validated_data['email'])
    if not user:
        return Response(
            status=status.HTTP_404_UNAUTHORIZED,
            data="Пользователь не найден"
        )
    
    send_change_email(user.email, create_nonce(user.email))

    return Response(
        status=status.HTTP_200_OK,
        data='Письмо для смены пароля отправлено на почту'
    )


@extend_schema(
    summary="Подтверждение смены пароля",
    request=PasswordChangeConfirmSerializer
)
@api_view(['POST'])
def password_change_confirm(request):
    serializer = PasswordChangeConfirmSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    
    email = get_email_by_nonce(serializer.validated_data['nonce'])
    if not email:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data="Одноразовый код не найден или устарел"
        )

    user = get_user_by_email(email)
    if not user:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data="Пользователь не найден"
        )
    
    user.set_password(serializer.validated_data['new_password'])
    user.save()

    return Response(
        status=status.HTTP_200_OK,
        data='Пароль успешно изменен'
    )