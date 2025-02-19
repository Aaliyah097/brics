from auth2.signup.views import signup, signup_confirm
from auth2.login.views import login2fa, login2fa_confirm
from auth2.password.views import password_change, password_change_confirm
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from django.urls import path


urlpatterns = [
    path('signup/', view=signup),
    path('signup/confirm/', view=signup_confirm),
    path('login2fa/', view=login2fa),
    path('login2fa/confirm/', view=login2fa_confirm),
    path('password-change/', view=password_change),
    path('password-change/confirm/', view=password_change_confirm),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
