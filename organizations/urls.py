from django.urls import path, include
from rest_framework.routers import DefaultRouter
from organizations.views import OrganizationViewSet

router = DefaultRouter()
router.register('', OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
