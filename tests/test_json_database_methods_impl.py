import unittest
from src.database_methods.json_database_methods_impl import JsonDatabaseMethodsImpl

class TestJsonDatabaseMethodsImpl(unittest.TestCase):
    
    json_db: JsonDatabaseMethodsImpl

    @classmethod
    def setUpClass(cls):
        cls.json_db = JsonDatabaseMethodsImpl()

    
    def test_add_user(self) -> None:
        self.json_db.add_user(user_id="132532523")
        self.json_db.add_user(user_id="3245324253464232")
        self.json_db.add_user(user_id="3645262456745")
        all_users = self.json_db.get_all_users()
        self.assertEquals(["132532523", "3245324253464232", "3645262456745"], all_users)
    
    def test_get_user_amount(self) -> None:
        size = self.json_db.get_users_amount()

        self.assertEquals(3, size)
        self.assertNotEquals(4, size)

if __name__ == "__main__":
    unittest.main()