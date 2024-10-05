from rest_framework.fields import ChoiceField
from rest_framework.serializers import ModelSerializer

from apps.job.models import JobAnnounce
from apps.job.tasks import create_notification_for_developers


#
# class JobLevelChoice=(
# ("junior", "Junior"),
# ("middle", "Middle"),
# ("senior", "Senior"),
#     LEAD = "lead", "Lead"
# )
#
# class JobTypeChoice(ChoiceField):
#     FIXED_PRICE = 'fixed_price', "Fixed Price"
#     HOURLY = 'hourly', "Hourly"
#
#
# class PriceMeasureChoice(ChoiceField):
#     UZS = "uzs", "UZS"
#     USD = "usd", "USD"


class JobAnnounceListCreateSerializer(ModelSerializer):
    # job_type = JobTypeChoice()
    # price_measure = PriceMeasureChoice()
    # level = JobLevelChoice()

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
            "technology",
            "profession",
            "location"
        )

    def create(self, validated_data):
        instance = super().create(validated_data)
        create_notification_for_developers.delay(instance_id=instance.id)
        return instance
