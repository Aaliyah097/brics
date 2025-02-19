from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from auth2.signup.serializers import SignupSerializer, SignupConfirmSerializer
from users.is_email_free import is_email_free
from users.create_new_user import create_new_user
from auth2.nonce.create_nonce import create_nonce
from auth2.signup.send_signup_email import send_signup_email
from auth2.nonce.get_email_by_nonce import get_email_by_nonce


@extend_schema(
    summary="Регистрация",
    request=SignupSerializer,
)
@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    
    email = serializer.validated_data['email']
    if not is_email_free(email):
        return Response(
            status=status.HTTP_409_CONFLICT,
            data='Почтовый адрес занят'
        )
    
    send_signup_email(email, create_nonce(email))
    
    return Response(
        status=status.HTTP_200_OK,
        data="Письмо для завершения регистрации отправлено на почту"
    )


@extend_schema(
    summary="Подтверждение регистрации",
    request=SignupConfirmSerializer
)
@api_view(['POST'])
def signup_confirm(request):
    serializer = SignupConfirmSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    email = get_email_by_nonce(serializer.validated_data['nonce'])
    if not email:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data="Одноразовыый код не найден, мб он истек"
        )
    
    new_user_id = create_new_user(email, serializer.validated_data['password'])

    return Response(
        status=status.HTTP_200_OK,
        data=f"Новый ползователь с ИД {new_user_id} создан"
    )
