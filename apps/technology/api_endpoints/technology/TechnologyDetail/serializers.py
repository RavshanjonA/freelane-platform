from rest_framework import serializers

from apps.technology.models import Technology


class TechnologyRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id','name']
