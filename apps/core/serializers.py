from django.contrib.sites.models import Site
from rest_framework_json_api import serializers


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('domain', 'name')
