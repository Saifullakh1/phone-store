from rest_framework import routers
from .views import ReviewAPIViewSet, FavoriteAPIViewSet

router = routers.DefaultRouter()

router.register(
    "reviews",
    ReviewAPIViewSet
)
router.register(
    "favorite",
    FavoriteAPIViewSet
)

urlpatterns = router.urls