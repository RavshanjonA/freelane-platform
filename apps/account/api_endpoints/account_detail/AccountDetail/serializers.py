from rest_framework import serializers

from apps.account.models import Account, AccountInfo
from apps.technology.models import Profession, Technology


class AccountInfoSerializer(serializers.ModelSerializer):
    profession = serializers.PrimaryKeyRelatedField(queryset=Profession.objects.all())
    technologies = serializers.PrimaryKeyRelatedField(queryset=Technology.objects.all(), many=True)

    class Meta:
        model = AccountInfo
        fields = ['bio', 'profession', 'technologies', 'is_visible']


class AccountDetailSerializer(serializers.ModelSerializer):
    account_info = AccountInfoSerializer()

    class Meta:
        model = Account
        fields = ['phone', 'account_info', 'role', 'email']

    def update(self, instance, validated_data):
        account_info_data = validated_data.pop('account_info', None)
        instance = super().update(instance, validated_data)

        if account_info_data:
            account_info = instance.account_info

            profession = account_info_data.get('profession')
            technologies = account_info_data.get('technologies')

            if profession:
                account_info.profession_id = profession

            if technologies:
                account_info.technologies.set(technologies)

            account_info.bio = account_info_data.get('bio', account_info.bio)
            account_info.is_visible = account_info_data.get('is_visible', account_info.is_visible)
            account_info.save()

        return instance
