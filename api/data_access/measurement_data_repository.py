from api.data_access.base import RepositoryBase
from api.models import MeasurementData


class MeasurementDataRepository(RepositoryBase):
    def __init__(self):
        super().__init__(MeasurementData)