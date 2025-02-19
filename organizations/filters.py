import django_filters
from django.contrib.postgres.search import SearchQuery
from organizations.models import Organizations


class OrganizationFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Organizations
        fields = [
            field.name 
            for field in Organizations._meta.get_fields() 
            if field.name not in ('search_vector')
        ] + ['search']

    def filter_search(self, queryset, name, value):
        search_query = SearchQuery(value)
        return queryset.filter(search_vector=search_query)
