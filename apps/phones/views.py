from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Phone
from .serializers import PhoneSerializer, PhoneListSerializer, PhoneDetailSerializer
from .filters import PhoneFilter


class PhoneAPIViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    filter_backends = [
        filters.DjangoFilterBackend
    ]
    filterset_fields = [
        "user"
    ]
    filterset_class = PhoneFilter

    def get_serializer_class(self):
        if self.action in "list":
            return PhoneListSerializer
        elif self.action in "retrieve":
            return PhoneDetailSerializer
        else:
            return self.serializer_class
