"""
Django settings for {{ project_name }} project.

Use in development.
"""

# pylint: disable = wildcard-import, unused-wildcard-import
from .base import *

CORS_ORIGIN_ALLOW_ALL = DEBUG

INTERNAL_IPS = ("127.0.0.1",)

ALLOWED_HOSTS += (
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
)
