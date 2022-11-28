"""
Django settings for project_name project.

Base settings.
"""

import datetime

# pylint: disable = wildcard-import, unused-wildcard-import
from .settings import *

if DEBUG is True:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }

INSTALLED_APPS += (
    # Django
    "django.contrib.sites",
    # Third-party
    "django_filters",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_json_api",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
    # Local
    "project_name.apps.core",
    "project_name.apps.users",
    "project_name.apps.todos",
)
AUTH_USER_MODEL = "users.User"
REST_USE_JWT = True
JWT_AUTH_COOKIE = "jwt-auth"

SITE_ID = DEFAULT_SITE_ID = os.environ.get("SITE_ID", 1)

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=10),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
}

PROJECT_NAME = "project_name"

TEMPLATES[0]["OPTIONS"]["context_processors"] = [
    "django.template.context_processors.debug",
    "django.template.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "project_name.apps.core.context_processors.sitewide",
]

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

LOGIN_URL = "accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework_json_api.pagination.PageNumberPagination",
    "DEFAULT_METADATA_CLASS": "rest_framework_json_api.metadata.JSONAPIMetadata",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.openapi.AutoSchema",
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES[0]["DIRS"] = [
    TEMPLATES_DIR,
]
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

STATICFILES_DIRS = (ASSETS_DIR,)

# JSON API serializer dasherizes attribute keys by default
JSON_API_FORMAT_FIELD_NAMES = "dasherize"

CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_FRAME_DENY = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
USE_X_FORWARDED_HOST = True
X_FRAME_OPTIONS = "DENY"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost").strip()
EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS", False))
EMAIL_PORT = int(os.environ.get("EMAIL_HOST_PORT", 25))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "").strip()
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "").strip()
DEFAULT_FROM_EMAIL = "Fixme Example <noreply@example.com>"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
