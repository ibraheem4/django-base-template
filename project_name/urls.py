"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.schemas.openapi import SchemaGenerator

from apps.api.views import api_router
from apps.core import views as core_views
from apps.users import views as user_views
from apps.core.urls import router as core_router
from apps.users.urls import router as users_router
from apps.todos.urls import router as todos_router

from patches import routers

apps_router = routers.DefaultRouter()
apps_router.extend(core_router)
apps_router.extend(users_router)
apps_router.extend(todos_router)

urlpatterns = [
    path("accounts/", include("allauth.urls"), name="socialaccount_signup"),
    path("api/", include(api_router.urls)),
    path("api/users/me/", user_views.CurrentUserView.as_view(), name="me"),
    path("api/session/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/dj-rest-auth/facebook/",
        user_views.FacebookLoginView.as_view(),
        name="fb_login",
    ),
    path(
        "api/dj-rest-auth/google/",
        user_views.GoogleLoginView.as_view(),
        name="google_login",
    ),
    path(
        "openapi/",
        get_schema_view(
            title="project_name API",
            description="API backend for project_name",
            version="1.0.0",
            generator_class=SchemaGenerator,
        ),
        name="openapi-schema",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls, name="admin"),
    path("", core_views.index, name="index"),
    path("", include(apps_router.urls)),
    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
