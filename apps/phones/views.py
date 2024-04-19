from rest_framework import viewsets
from .models import Phone
from .serializers import PhoneSerializer


class PhoneAPIViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

