from rest_framework import serializers
from .models import Phone
from apps.images.serializers import ImageSerializer


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ("id", "name", "description",
                  "color", "memory", "model",
                  "image", "price", "currency",
                  "company", "published")


class PhoneListSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)

    class Meta:
        model = Phone
        fields = ("id", "name",
                  "color", "memory", "model",
                  "image", "price", "currency",
                  "is_exists", "is_active")


class PhoneDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)

    class Meta:
        model = Phone
        fields = ("id", "name", "description",
                  "color", "memory", "model",
                  "image", "price", "currency",
                  "company", "ratings", "published",
                  "is_exists", "is_active")

