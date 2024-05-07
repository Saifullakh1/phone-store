from rest_framework import serializers
from .models import Review, Favorite, Like


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "phone", "user", "comment", "rating", "published_date", "is_active")


class ReviewListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ("id", "phone", "user", "name", "comment", "rating", "published_date", "is_active", "likes", "dislikes")

    def get_likes(self, obj):
        likes = Like.objects.filter(review=obj, is_like=True).count()
        return likes

    def get_dislikes(self, obj):
        likes = Like.objects.filter(review=obj, is_like=False).count()
        return likes



class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ("id", "user", "phone")


class FavoriteListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='phone.name')
    color = serializers.CharField(source='phone.color')
    model = serializers.CharField(source='phone.model')
    price = serializers.CharField(source='phone.price')
    currency = serializers.CharField(source='phone.currency')

    class Meta:
        model = Favorite
        fields = ("id", "user", "phone", "name", "color",
                  "model", "price", "currency",)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "review", "user", "is_like")

