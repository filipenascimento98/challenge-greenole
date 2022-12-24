from django.db import models
from uuid import uuid4


class MeasurementData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sensor_id = models.BigIntegerField("ID Sensor")
    measured_at = models.DateTimeField("Measured at")
    value = models.IntegerField("Value")
    created_at = models.DateTimeField("Created at", auto_now_add=True)

class DuplicateMeasurementData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    measurement_data = models.ForeignKey(
        "MeasurementData",
        verbose_name= "Duplicate measurement data",
        related_name= "duplicate_data",
        on_delete=models.CASCADE
    )