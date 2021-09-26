from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import FieldWorker
from .serializers import FieldWorkerSerializer

# Create your views here.


class FieldWorkerViewSet(ModelViewSet):
    serializer_class = FieldWorkerSerializer
    queryset = FieldWorker.objects.all()
    permission_classes = [AllowAny]
