from rest_framework.viewsets import ModelViewSet

from .models import People
from .serializers import PeopleSerializer


class PeopleViewSet(ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def list(self, request, *args, **kwargs):
        self.queryset = People.objects.filter(
            **{f'{key}__contains': value for key, value in request.GET.items()}
        ).all()
        return super().list(request, *args, **kwargs)
