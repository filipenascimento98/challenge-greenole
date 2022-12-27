from rest_framework import serializers


class MeasurementDataSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField()
    measured_at = serializers.DateTimeField()
    value = serializers.IntegerField()

class ListMeasurementDataSerializer(serializers.Serializer):
    time = serializers.ChoiceField(choices=['minute', 'hour', 'day'])
    value = serializers.CharField(min_length=1, max_length=2)