from django_filters import rest_framework as filters
from .models import Review, Favorite


class ReviewFilter(filters.FilterSet):
    class Meta:
        model = Review
        fields = ["phone", ]


class FavoriteFilter(filters.FilterSet):
    class Meta:
        model = Favorite
        fields = ["user", ]

