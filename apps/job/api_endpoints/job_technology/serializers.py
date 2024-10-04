from rest_framework import serializers
from apps.job.models import JobTechnology
from apps.technology.models import Technology


class JobTechnologySerializer(serializers.ModelSerializer):
    technology_id = serializers.PrimaryKeyRelatedField(queryset=Technology.objects.all(), source='technology')

    class Meta:
        model = JobTechnology
        fields = ['technology_id', 'level']


class JobTechnologyReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTechnology
        fields = ['technology', 'level']