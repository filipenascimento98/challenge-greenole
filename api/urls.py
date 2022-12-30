from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views.user import UserView
from api.views.measurement_data import MeasurementDataView

schema_view = get_schema_view(
   openapi.Info(
      title="Greenole API",
      default_version='v1',
      description="Greenole API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="filipe.almeida@dcomp.ufs.br"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'user', UserView, basename='user')
router.register(r'measurement', MeasurementDataView, basename='measurement')

urlpatterns = [
    path("login/", obtain_auth_token, name='login'),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs')
]