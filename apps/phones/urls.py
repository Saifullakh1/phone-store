from rest_framework import routers
from .views import PhoneAPIViewSet


router = routers.DefaultRouter()

router.register(
    "phones",
    PhoneAPIViewSet
)

urlpatterns = router.urls
