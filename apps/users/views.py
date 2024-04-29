from rest_framework import viewsets
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer, UserDetailSerializer


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in 'update' or self.action in 'retrieve':
            return UserDetailSerializer
        return self.serializer_class

