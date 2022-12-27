from datetime import datetime, timedelta
import logging

from api.domain.base import DomainBase
from api.data_access.measurement_data_repository import MeasurementDataRepository


class MeasurementDataDomain(DomainBase):
    def __init__(self):
        super().__init__(MeasurementDataRepository())
    
    def _validate_data(self, value, time):
        if time == 'minute':
            if value in range(0, 60):
                return True
        elif time == 'hour': 
            if value in range(0, 24):
                return True
        else:
            if value in range(1, 32):
                return True
        
        return False

    def list(self, value, time):
        try:
            value = int(value)
            if value < 0:
                return ("Value must be positive integer.", 406)
        except Exception as e:
            logging.error(e)
            return ("Value must be positive integer.", 406)
        
        # Validação do parâmetro value
        success = self._validate_data(value, time)

        if not success:
            return ("Incorrect input to parameter 'value'.", 406)
        
        # Geração da datetime para filtragem no banco
        now = datetime.now()
        if time == 'minute':
            datetime_to_search = now - timedelta(minutes=value)
        elif time == 'hour': 
            datetime_to_search = now - timedelta(hours=value)
        else:
            datetime_to_search = now - timedelta(days=value)
        
        try:
            measurements_data = self.repository.filter_by_created_at(datetime_to_search)
        except Exception as e:
            logging.error(e)
            return ("Error querying the data in the database", 500)
        
        data = []
        for measurement_data in measurements_data:
            data.append({
                "id": measurement_data.id,
                "sensor_id": measurement_data.sensor_id,
                "measured_at": measurement_data.measured_at,
                "value": measurement_data.value,
                "created_at": measurement_data.created_at
            })

        return data