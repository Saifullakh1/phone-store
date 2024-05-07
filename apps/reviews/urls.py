from rest_framework import routers
from .views import ReviewAPIViewSet, FavoriteAPIViewSet, LikeAPIViewSet

router = routers.DefaultRouter()

router.register(
    "reviews",
    ReviewAPIViewSet
)
router.register(
    "favorite",
    FavoriteAPIViewSet
)
router.register(
    "like",
    LikeAPIViewSet
)

urlpatterns = router.urls