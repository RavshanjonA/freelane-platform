from django.contrib.postgres.search import TrigramSimilarity
from rest_framework import filters


class TrigramSearchFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search = request.query_params.get('search', None)
        if search:
            queryset = queryset.annotate(
                similarity=TrigramSimilarity('name', search)
            ).filter(similarity__gt=0.2).order_by('-similarity')

        return queryset
