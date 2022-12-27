from api.data_access.base import RepositoryBase
from api.models import MeasurementData


class MeasurementDataRepository(RepositoryBase):
    def __init__(self):
        super().__init__(MeasurementData)
    
    def filter_by_created_at(self, date):
        '''
        Realiza a filtragem dos registros em banco que tem data de criação maiores
        do que a passada como parâmetro.
        Args:
        - date: Data a ser filtrada
        Returns:
        - Todos os registros que tem o campo created_at com data maior do que 'date'.
        '''
        return self.model.objects.filter(created_at__gt=date)