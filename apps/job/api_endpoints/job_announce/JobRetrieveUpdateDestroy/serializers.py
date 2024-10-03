from rest_framework import serializers

from apps.job.models import JobAnnounce


class JobAnnounceRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAnnounce
        fields = (
            "id",
            "title",
            "body",
            "job_type",
            "price",
            "price_measure",
            "level",
            "payment_verified",
            "technology",
            "profession",
            "location"
        )
