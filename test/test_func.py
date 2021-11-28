import unittest
import main.main
from main.main import setRoles, setUsers


class TestInput(unittest.TestCase):
    def setUp(self):
        main.main.roles_li = []
        main.main.users_li = []

    def test_emptyroles(self):
        empty_roles = []
        self.assertFalse(main.main.roles_li, "Input role is empty")
        setRoles(empty_roles)
        self.assertFalse(main.main.roles_li, "Input role is empty")

    def test_onerole(self):
        roles = [{"Id": 1, "Name": "System Administrator", "Parent": 0}]
        self.assertFalse(main.main.roles_li, "Initialize empty role")
        setRoles(roles)
        self.assertEqual(1, len(main.main.roles_li), "Input role contains 1 role only")
        self.assertEqual("System Administrator", main.main.roles_li[0].Name)

    def test_roles(self):
        roles = [
            {"Id": 1, "Name": "System Administrator", "Parent": 0},
            {
                "Id": 2,
                "Name": "Location Manager",
                "Parent": 1,
            },
            {
                "Id": 3,
                "Name": "Supervisor",
                "Parent": 2,
            },
            {
                "Id": 4,
                "Name": "Employee",
                "Parent": 3,
            },
            {
                "Id": 5,
                "Name": "Trainer",
                "Parent": 3,
            },
        ]
        self.assertFalse(main.main.roles_li, "Initialize empty role")
        setRoles(roles)
        self.assertEqual(5, len(main.main.roles_li), "Input role contains 5 roles")
        self.assertEqual("Location Manager", main.main.roles_li[1].Name)

    def test_users(self):
        empty_users = []
        self.assertFalse(main.main.users_li, "Input user is empty")
        setRoles(empty_users)
        self.assertFalse(main.main.users_li, "Input user is empty")

    def test_oneuser(self):
        users = [{"Id": 1, "Name": "Adam Admin", "Role": 1}]
        self.assertFalse(main.main.users_li, "Initialize empty user")
        setUsers(users)
        self.assertEqual(1, len(main.main.users_li), "Input user contains 1 user only")
        self.assertEqual(
            "Adam Admin", main.main.users_li[0].Name, "Test user with name Adam Admin"
        )

    def test_users(self):
        users = [
            {"Id": 1, "Name": "Adam Admin", "Role": 1},
            {"Id": 2, "Name": "Emily Employee", "Role": 4},
            {"Id": 3, "Name": "Sam Supervisor", "Role": 3},
            {"Id": 4, "Name": "Mary Manager", "Role": 2},
            {"Id": 5, "Name": "Steve Trainer", "Role": 5},
        ]
        self.assertFalse(main.main.users_li, "Initialize empty user")
        setUsers(users)
        self.assertEqual(5, len(main.main.users_li), "Input user contains 5 users")
        self.assertEqual(
            "Sam Supervisor",
            main.main.users_li[2].Name,
            "Test user with name Sam Supervisor",
        )


if __name__ == "__main__":
    unittest.main()
