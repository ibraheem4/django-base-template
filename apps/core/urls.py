from django.urls import path, include
from rest_framework import routers
from .views import SiteViewSet

router = routers.SimpleRouter()
router.register(r"api/sites", SiteViewSet)

urlpatterns = router.urls

urlpatterns = [path("", include(router.urls))]
