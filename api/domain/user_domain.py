from api.domain.base import DomainBase
from api.data_access.user_repository import UserRepository


class UserDomain(DomainBase):
    def __init__(self):
        super().__init__(UserRepository())