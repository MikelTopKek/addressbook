from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

from .models import People


class PeopleSerializer(ModelSerializer):
    class Meta:
        model = People
        fields = ['id', 'name', 'surname', 'address', 'telephone', 'url']
