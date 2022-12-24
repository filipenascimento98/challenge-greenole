from api.domain.base import DomainBase
from api.data_access.measurement_data_repository import MeasurementDataRepository


class MeasurementDataDomain(DomainBase):
    def __init__(self):
        super().__init__(MeasurementDataRepository())