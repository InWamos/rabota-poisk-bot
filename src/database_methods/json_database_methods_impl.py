import datetime
import json

from typing import Any
from database_methods.database_methods import DatabaseMethods


class JsonDatabaseMethodsImpl(DatabaseMethods):
    PATH_TO_DB: str = "data/db/users.json"

    def add_user(self, user_id: str) -> None:
        table: dict[str, dict[str, Any]] = self._get_json_data()

        if not user_id in table.keys():
            user: dict[str, Any] = {
                "date": datetime.datetime.now().isoformat(),
                "isBanned": False,
            }
            table[user_id] = user

            self._write_json_data(table=table)

    def get_users_amount(self) -> int:
        table = self._get_json_data()
        return len(table.keys())

    def set_user_banned(self, user_id: str) -> None:
        table = self._get_json_data()
        table[user_id]["isBanned"] = True
        self._write_json_data(table=table)

    def get_all_users(self) -> list[str]:
        table: dict[str, dict[str, Any]] = self._get_json_data()
        return list(table.keys())

    def _get_json_data(self) -> dict[str, dict[str, Any]]:
        with open(file=self.PATH_TO_DB, mode="r") as json_file:
            return json.load(json_file)

    def _write_json_data(self, table: dict[str, dict[str, Any]]) -> None:
        with open(self.PATH_TO_DB, "w") as json_file:
            json.dump(table, json_file, indent=4)
