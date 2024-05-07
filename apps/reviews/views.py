from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters

from .models import Review, Favorite, Like
from .serializers import ReviewSerializer, ReviewListSerializer, FavoriteSerializer, FavoriteListSerializer, LikeSerializer
from .filters import ReviewFilter, FavoriteFilter


class ReviewAPIViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [
        filters.DjangoFilterBackend
    ]
    filterset_fields = [
        "phone"
    ]
    filterset_class = ReviewFilter

    def get_serializer_class(self):
        if self.action in 'list':
            return ReviewListSerializer
        return self.serializer_class


class FavoriteAPIViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [
        filters.DjangoFilterBackend
    ]
    filterset_fields = [
        "user"
    ]
    filterset_class = FavoriteFilter

    def get_serializer_class(self):
        if self.action in 'list':
            return FavoriteListSerializer
        return self.serializer_class


class LikeAPIViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer