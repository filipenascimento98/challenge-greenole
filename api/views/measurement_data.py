from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from api.domain.measurement_data_domain import MeasurementDataDomain
from api.serializers.measurement_data import MeasurementDataSerializer 


class MeasurementDataView(GenericViewSet, 
    mixins.CreateModelMixin, mixins.ListModelMixin):

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    domain = MeasurementDataDomain()

    def create(self, request, *args, **kwargs):
        serializer = MeasurementDataSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = self.domain.create(serializer.data)
        
        return Response(status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        print(request.query_params)

        return Response(status=status.HTTP_200_OK)