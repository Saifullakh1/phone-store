from rest_framework import routers
from .views import ReviewAPIViewSet

router = routers.DefaultRouter()

router.register(
    "reviews",
    ReviewAPIViewSet
)

urlpatterns = router.urls