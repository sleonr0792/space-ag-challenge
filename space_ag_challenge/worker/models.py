import uuid

from django.db import models

PRUNING = "PR"
HARVEST = "HA"
SCOUTING = "SC"
OTHER = "OT"

FUNCTION_CHOICES = (
    (PRUNING, "Pruning"),
    (HARVEST, "Harvest"),
    (SCOUTING, "Scouting"),
    (OTHER, "Other"),
)


class FieldWorker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    function = models.CharField(max_length=2, choices=FUNCTION_CHOICES, default=OTHER)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
