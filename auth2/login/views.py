from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from auth2.login.serializers import Login2faConfirmSerializer, Login2faSerializer, TokensPairSerializer
from auth2.nonce.create_nonce import create_nonce
from auth2.login.send_2fa_email import send_2fa_email
from auth2.nonce.get_email_by_nonce import get_email_by_nonce
from users.get_user_by_email import get_user_by_email
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


@extend_schema(
    summary="Вход 2-фактор",
    request=Login2faSerializer
)
@api_view(['POST'])
def login2fa(request):
    serializer = Login2faSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    user = authenticate(
        email=serializer.validated_data['email'], 
        password=serializer.validated_data['password']
    )
    if not user:
        return Response(
            status=status.HTTP_404_UNAUTHORIZED,
            data="Пользователь не найден"
        )
    
    send_2fa_email(user.email, create_nonce(user.email))

    return Response(
        status=status.HTTP_200_OK,
        data='Письмо для подтверждения входа отправлено на почту'
    )


@extend_schema(
    summary="Подтверждение входа",
    request=Login2faConfirmSerializer,
    responses=TokensPairSerializer
)
@api_view(['POST'])
def login2fa_confirm(request):
    serializer = Login2faConfirmSerializer(data=request.data)
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

    return Response(
        status=status.HTTP_200_OK,
        data=TokensPairSerializer(
            {
                'access': str(AccessToken.for_user(user)),
                'refresh': str(RefreshToken.for_user(user))
            }
        ).data
    )

