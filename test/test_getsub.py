import unittest
import main.main
from main.main import setRoles, setUsers, getSubOrdinates


class TestGetsub(unittest.TestCase):
    def setUp(self):
        main.main.roles_li = []
        main.main.users_li = []

    def test_empty_roles_users(self):
        roles = []
        users = []
        setRoles(roles)
        setUsers(users)
        output = getSubOrdinates(1)
        self.assertFalse(output, "Expected empty list")

    def test_empty_roles(self):
        roles = []
        users = [
            {"Id": 1, "Name": "Adam Admin", "Role": 1},
            {"Id": 2, "Name": "Emily Employee", "Role": 4},
        ]
        setRoles(roles)
        setUsers(users)
        output = getSubOrdinates(1)
        self.assertFalse(output, "Expected empty list")

    def test_empty_users(self):
        roles = [
            {"Id": 1, "Name": "System Administrator", "Parent": 0},
            {
                "Id": 2,
                "Name": "Location Manager",
                "Parent": 1,
            },
        ]
        users = []
        setRoles(roles)
        setUsers(users)
        output = getSubOrdinates(1)
        self.assertFalse(output, "Expected empty list")

    def test_getsub(self):
        roles = [
            {"Id": 1, "Name": "System Administrator", "Parent": 0},
            {
                "Id": 2,
                "Name": "Location Manager",
                "Parent": 1,
            },
        ]
        users = [
            {"Id": 1, "Name": "Adam Admin", "Role": 1},
            {"Id": 2, "Name": "Emily Employee", "Role": 4},
        ]
        setRoles(roles)
        setUsers(users)
        output = getSubOrdinates(1)
        self.assertFalse(output, "Expected empty list")

        roles = [
            {"Id": 1, "Name": "System Administrator", "Parent": 0},
            {
                "Id": 2,
                "Name": "Location Manager",
                "Parent": 1,
            },
        ]
        users = [
            {"Id": 1, "Name": "Adam Admin", "Role": 1},
            {"Id": 2, "Name": "Emily Employee", "Role": 4},
            {"Id": 4, "Name": "Mary Manager", "Role": 2},
        ]
        setRoles(roles)
        setUsers(users)
        output = getSubOrdinates(1)
        self.assertEqual(
            [{"Id": 4, "Name": "Mary Manager", "Role": 2}],
            output,
            "Expected returning Manger in the list",
        )

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
        users = [
            {"Id": 1, "Name": "Adam Admin", "Role": 1},
            {"Id": 2, "Name": "Emily Employee", "Role": 4},
            {"Id": 3, "Name": "Sam Supervisor", "Role": 3},
            {"Id": 4, "Name": "Mary Manager", "Role": 2},
            {"Id": 5, "Name": "Steve Trainer", "Role": 5},
        ]
        setRoles(roles)
        setUsers(users)
        output = getSubOrdinates(4)
        self.assertEqual(
            [
                {"Id": 2, "Name": "Emily Employee", "Role": 4},
                {"Id": 3, "Name": "Sam Supervisor", "Role": 3},
                {"Id": 5, "Name": "Steve Trainer", "Role": 5},
            ],
            output,
            "Expected returning 3 users in the list",
        )


if __name__ == "__main__":
    unittest.main()
