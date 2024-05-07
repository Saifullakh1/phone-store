from django.contrib import admin
from .models import Review, Favorite, Like


admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Like)