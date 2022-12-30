from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from api.domain.measurement_data_domain import MeasurementDataDomain
from api.serializers.measurement_data import (
    MeasurementDataSerializer,
    ListMeasurementDataSerializer,
    ResponseListMeasurementDataSerializer
)
from api.task import create


class MeasurementDataView(GenericViewSet, 
    mixins.CreateModelMixin, mixins.ListModelMixin):

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    domain = MeasurementDataDomain()

    @swagger_auto_schema(request_body= MeasurementDataSerializer(), 
        responses={
            201: "No content", 
            406: "'Value must be positive integer'. or 'Incorrect input to parameter 'value'.'", 
            500: "Error querying the data in the database"}
    )
    def create(self, request, *args, **kwargs):
        serializer = MeasurementDataSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            try:
                create.delay(serializer.data)
            except Exception as e:
                return Response({
                    'message': 'An unexpected error occurred.'}, 
                    status=status.HTTP_412_PRECONDITION_FAILED
                )
        
        return Response(status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(query_serializer=ListMeasurementDataSerializer(),responses={200: ResponseListMeasurementDataSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        value = request.query_params.get('value', None)
        time = request.query_params.get('time', None)
        
        serializer = ListMeasurementDataSerializer(data={'value': value, 'time': time})

        if serializer.is_valid(raise_exception=True):
            try:
                ret = self.domain.list(value, time)
            except Exception as e:
                return Response({
                    'message': 'An unexpected error occurred.'}, 
                    status=status.HTTP_412_PRECONDITION_FAILED
                )
        
        if isinstance(ret, tuple):
            return Response({'message': ret[0]}, status=ret[1])
        
        return Response(ret, status=status.HTTP_200_OK)