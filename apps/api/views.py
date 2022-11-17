from rest_framework import routers

from apps.core.views import SiteViewSet

# Register the API viewset
api_router = routers.DefaultRouter(trailing_slash=False)

# project_name API routes
api_router.register(r"sites", SiteViewSet)
