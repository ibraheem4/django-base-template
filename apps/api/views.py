from rest_framework import routers

from apps.core.views import SiteViewSet
from apps.users.views import UserViewSet

# Register the API viewset
api_router = routers.DefaultRouter(trailing_slash=False)

# project_name API routes
api_router.register(r"users", UserViewSet)
api_router.register(r"sites", SiteViewSet)
