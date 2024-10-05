from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.technology.models import Technology


class TechnologyListCreateSerializer(ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'name')

    def validate(self, attr):
        slug = slugify(attr["name"])
        if Technology.objects.filter(slug=slug).exists():
            raise ValidationError(detail={'name': 'This  technology already created'}, code="name")
        return attr

    def create(self, validated_data):
        technolgy = super().create(validated_data)
        technolgy.slug = slugify(technolgy.name)
        technolgy.save()
        return technolgy
