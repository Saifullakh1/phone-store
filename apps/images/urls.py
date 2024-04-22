from rest_framework import routers
from .views import ImageAPIViewSet


router = routers.DefaultRouter()
router.register(
    "images",
    ImageAPIViewSet
)


urlpatterns = router.urls
