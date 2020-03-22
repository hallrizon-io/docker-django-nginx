from rest_framework import serializers
from api.users.models import Profile
from typing import OrderedDict


class ProfileDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username',
                  'email',
                  'client',
                  'demo',
                  'phone',
                  'first_name',
                  'last_name', ]

    def validate(self, attrs: OrderedDict):
        attrs = super().validate(attrs)
        if self.context['request'].method == "POST":
            try:
                if self.context['request'].data['password'] != self.context['request'].data['password_verify']:
                    raise serializers.ValidationError({
                        'password': 'Паролі не співпадають.'
                    })
                attrs.update({'password': self.context['request'].data['password']})
            except KeyError:
                raise serializers.ValidationError({
                    'password': 'Введіть пароль.'
                })

        return attrs

    def create(self, validated_data):
        validated_data = dict(self._validated_data)
        password = validated_data.pop('password')

        profile = Profile.objects.create(**validated_data)
        profile.set_password(password)
        profile.save()

        return profile
