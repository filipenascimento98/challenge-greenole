from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from api.views.user import UserView
from api.views.measurement_data import MeasurementDataView


app_name = "api"

router = routers.DefaultRouter()
router.register(r'user', UserView, basename='user')
router.register(r'measurement', MeasurementDataView, basename='measurement')

urlpatterns = [
    path("login/", obtain_auth_token),
    path('', include(router.urls))
]