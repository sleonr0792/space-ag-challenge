from rest_framework import routers

from .views import FieldWorkerViewSet

app_name = "field-workers"

router = routers.DefaultRouter()
router.register(r"field_workers", FieldWorkerViewSet, basename="field-workers")

urlpatterns = []
urlpatterns += router.urls
