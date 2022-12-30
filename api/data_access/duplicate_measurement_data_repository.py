from api.data_access.base import RepositoryBase
from api.models import DuplicateMeasurementData


class DuplicateMeasurementDataRepository(RepositoryBase):
    def __init__(self):
        super().__init__(DuplicateMeasurementData)