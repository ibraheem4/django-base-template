from django.conf import settings


def sitewide(request):
    return {
        "settings": settings,
    }
