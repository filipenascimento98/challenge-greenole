from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.domain.user_domain import UserDomain
from api.serializers.user import UsuarioSerializer


class UserService(GenericViewSet, mixins.CreateModelMixin):
    domain = UserDomain()
    
    queryset = domain.list()
    serializer_class = UsuarioSerializer