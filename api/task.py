from api.domain.measurement_data_domain import MeasurementDataDomain
from celery import shared_task

@shared_task
def create(data):
    domain = MeasurementDataDomain()
    domain.create(data=data)