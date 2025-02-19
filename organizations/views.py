from django_filters.rest_framework import DjangoFilterBackend
from organizations.filters import OrganizationFilter
from rest_framework import viewsets
from organizations.models import Organizations
from organizations.serializer import OrganizationSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from organizations.create_organizations import create_organization
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrganizationFilter
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.errors
            )
        
        new_org_id = create_organization(serializer.validated_data, request.user.id)
        if not new_org_id:
            return Response(
                status=status.HTTP_409_CONFLICT,
                data='Организация с таким название уже существует в системе'
            )

        return Response(
            status=status.HTTP_200_OK,
            data=f"Создана новая организация с ИД {new_org_id}"
        )
    
    @extend_schema(
        summary="Список моих организаций",
        responses=OrganizationSerializer(many=True)
    )
    @action(methods=['GET', ], detail=False, url_path='my')
    def my(self, request):
        my_organizations = Organizations.objects.filter(members__in=(request.user, ))
        serializer = self.serializer_class(my_organizations, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
