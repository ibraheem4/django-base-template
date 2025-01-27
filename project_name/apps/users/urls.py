from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r"api/users", UserViewSet)

urlpatterns = router.urls

urlpatterns = [path("", include(router.urls))]
