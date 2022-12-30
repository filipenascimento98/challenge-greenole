from api.data_access.base import RepositoryBase
from django.contrib.auth.models import User

class UserRepository(RepositoryBase):
    def __init__(self):
        super().__init__(User)