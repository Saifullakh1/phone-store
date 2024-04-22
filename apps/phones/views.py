from rest_framework import viewsets
from .models import Phone
from .serializers import PhoneSerializer, PhoneListSerializer, PhoneDetailSerializer


class PhoneAPIViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    def get_serializer_class(self):
        if self.action in "list":
            return PhoneListSerializer
        elif self.action in "retrieve":
            return PhoneDetailSerializer
        else:
            return self.serializer_class
