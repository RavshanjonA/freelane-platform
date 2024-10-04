from rest_framework.serializers import ModelSerializer
from apps.job.api_endpoints.job_technology.serializers import JobTechnologySerializer, JobTechnologyReadSerializer
from apps.job.models import JobTechnology, JobAnnounce
from apps.job.tasks import create_notification_for_developers


class JobAnnounceListCreateSerializer(ModelSerializer):
    technology = JobTechnologySerializer(many=True, write_only=True)
    technologies = JobTechnologyReadSerializer(source='jobtechnology_set', many=True, read_only=True)

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
            "technology", # post/patch
            "technologies", # get
            "profession",
            "location"
        )

    def create(self, validated_data):
        technologies_data = validated_data.pop('technology')
        job_announce = super().create(validated_data)

        for technology_data in technologies_data:
            JobTechnology.objects.create(
                job=job_announce,
                technology=technology_data['technology'],
                level=technology_data['level']
            )

        create_notification_for_developers.delay(instance_id=job_announce.id)
        return job_announce
