from abc import ABC, abstractmethod
import datetime


class DatabaseMethods(ABC):
    @abstractmethod
    def increment_counter(self) -> None:
        pass

    @abstractmethod
    def add_user(self, user_id: int, date_added: datetime.datetime) -> None:
        pass
