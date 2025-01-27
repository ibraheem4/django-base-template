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
from django.views.generic import RedirectView
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.schemas.openapi import SchemaGenerator

from project_name.apps.core.urls import router as core_router
from project_name.apps.users.urls import router as users_router
from project_name.apps.todos.urls import router as todos_router
from project_name.apps.users import views as user_views

from patches import routers

apps_router = routers.DefaultRouter(trailing_slash=False)
apps_router.extend(core_router)
apps_router.extend(users_router)
apps_router.extend(todos_router)


urlpatterns = [
    path("", RedirectView.as_view(url="/api/", permanent=True)),
    path("accounts/", include("allauth.urls"), name="socialaccount_signup"),
    path("api/session/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/auth/", include("dj_rest_auth.urls")),
    path(
        "api/auth/registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    path("api/users/me/", user_views.CurrentUserView.as_view(), name="me"),
    path(
        "api/auth/facebook/",
        user_views.FacebookLoginView.as_view(),
        name="fb_login",
    ),
    path(
        "api/auth/google/",
        user_views.GoogleLoginView.as_view(),
        name="google_login",
    ),
    path(
        "api/",
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
    path("api/", include("project_name.apps.api.urls")),
    path("", include(apps_router.urls)),
    prefix_default_language=False,
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
