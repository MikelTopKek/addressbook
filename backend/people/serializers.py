import json

from rest_framework.serializers import ModelSerializer, RelatedField
from rest_framework.serializers import ValidationError

from .models import People, Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'country', 'city')


class PeopleSerializer(ModelSerializer):
    address = AddressSerializer(required=False, allow_null=True)

    def validate_url(self, value):
        if value and not value.startswith('http'):
            raise ValidationError('Should start from http')
        return value

    def create(self, validated_data):
        if 'address' in validated_data:
            address_data = validated_data.pop('address')
        elif self.initial_data.get('address'):
            address_data = json.loads(self.initial_data['address'])
        else:
            address_data = None
        
        if address_data and any(address_data.values()):
            address = Address.objects.create(**address_data)
        else:
            address = None
        
        new_people = People.objects.create(address=address, **validated_data)
        return new_people

    def update(self, instance, validated_data):
        if 'address' in validated_data:
            address_data = validated_data.pop('address')
        elif self.initial_data.get('address'):
            address_data = json.loads(self.initial_data['address'])
        else:
            address_data = None
        
        people = super().update(instance, validated_data)

        if address_data and any(address_data.values()):
            address = super().update(people.address, address_data)
        else:
            address = None
        
        people.address = address
        return people

    class Meta:
        model = People
        fields = (
            'id', 'name', 'surname', 'address',
            'telephone', 'url', 'image'
        )
