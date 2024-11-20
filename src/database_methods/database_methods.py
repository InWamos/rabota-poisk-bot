from abc import ABC, abstractmethod


class DatabaseMethods(ABC):
    @abstractmethod
    def add_user(self, user_id: str) -> None:
        pass

    @abstractmethod
    def get_users_amount(self) -> int:
        pass

    @abstractmethod
    def set_user_banned(self, user_id: str) -> None:
        pass
    
    @abstractmethod
    def get_all_users(self) -> list[str]:
        pass