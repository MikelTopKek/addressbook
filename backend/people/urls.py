from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('people', PeopleViewSet)

urlpatterns = router.urls
