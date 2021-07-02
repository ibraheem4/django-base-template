from rest_framework import routers
from apps.users.views import UserListView
from apps.core.views import SiteListView

# Register the API viewset
api_router = routers.DefaultRouter(trailing_slash=False)

# {{ project_name }} API routes
api_router.register(r'users', UserListView)
api_router.register(r'sites', SiteListView)
