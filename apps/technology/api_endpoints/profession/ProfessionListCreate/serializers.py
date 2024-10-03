from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.technology.models import Profession


class ProfessionListCreateSerializer(ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'name')

    def create(self, validated_data):
        profession = super().create(validated_data)
        profession.slug = slugify(profession.name)
        profession.save()
        return profession

    def validate(self, attr):
        slug = slugify(attr["name"])
        if Profession.objects.filter(slug=slug).exists():
            raise ValidationError(detail={'name': 'This  profession already created'}, code="name")
        return attr
