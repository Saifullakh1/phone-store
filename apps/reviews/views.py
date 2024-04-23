from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Review
from .serializers import ReviewSerializer
from .filters import ReviewFilter


class ReviewAPIViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [
        filters.DjangoFilterBackend
    ]
    filterset_fields = [
        "phone"
    ]
    filterset_class = ReviewFilter
