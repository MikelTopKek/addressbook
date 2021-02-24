from rest_framework.viewsets import ModelViewSet

from .models import People
from .serializers import PeopleSerializer


class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
