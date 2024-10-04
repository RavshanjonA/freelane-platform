from rest_framework import serializers

from apps.technology.models import Profession


class ProfessionRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id','name']
