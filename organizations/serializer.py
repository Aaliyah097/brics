from rest_framework import serializers
from organizations.models import Organizations


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = [
            field.name 
            for field in Organizations._meta.get_fields() 
            if field.name not in ('search_vector', 'organizationsmembers')
        ]
