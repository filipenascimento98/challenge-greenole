from rest_framework import serializers


class MeasurementDataSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField()
    measured_at = serializers.DateTimeField()
    value = serializers.IntegerField()