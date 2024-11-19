import datetime
from abc import ABC, abstractmethod


class DatabaseMethods(ABC):
    @abstractmethod
    def add_user(self, user_id: int, date_added: datetime.datetime) -> None:
        pass

    @abstractmethod
    def get_users_amount(self) -> int:
        pass
