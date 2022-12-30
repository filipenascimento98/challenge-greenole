from django.db import models
from uuid import uuid4


class CommomData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sensor_id = models.BigIntegerField("ID Sensor")
    measured_at = models.DateTimeField("Measured at")
    value = models.IntegerField("Value")
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        abstract = True
        
class MeasurementData(CommomData):
    class Meta:
        db_table = 'measurement_data'

class DuplicateMeasurementData(CommomData):
    class Meta:
        db_table = 'duplicate_measurement_data'