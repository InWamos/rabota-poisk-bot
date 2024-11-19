import datetime
import json

from typing import Any
from src.database_methods.database_methods import DatabaseMethods


class JsonDatabaseMethodsImpl(DatabaseMethods):
    PATH_TO_DB: str = "data/db/users.json"

    def add_user(self, user_id: int, date_added: datetime.datetime) -> None:
        pass

    def get_users_amount(self) -> int:
        return 0

    def _get_json_data(self) -> dict[int, dict[str, Any]]:
        with open(file=self.PATH_TO_DB, mode="r") as json_file:
            return json.load(json_file)

    def _is_user_exists(self, user_id: int) -> bool:
        table = self._get_json_data()
        return user_id in table.keys()