class Roles(object):
    def __init__(self, role):
        self.Id = role.get("Id")
        self.Name = role.get("Name")
        self.Parent = role.get("Parent")


class Users(object):
    def __init__(self, user):
        self.Id = user.get("Id")
        self.Name = user.get("Name")
        self.Role = user.get("Role")
        self.parent = None

    def __str__(self):
        return str({"Id": self.Id, "Name": self.Name, "Role": self.Role})


roles_li = []


def setRoles(roles_in):
    global roles_li
    roles_li = [Roles(role_in) for role_in in roles_in]
    return None


users_li = []


def setUsers(users_in):
    global users_li
    users_li = [Users(user_in) for user_in in users_in]
    return None


def getSubOrdinates(rank):
    check_role = 0
    for us in users_li:
        for ro in roles_li:
            if us.Role == ro.Id:
                us.parent = ro.Parent
                if us.Id == rank:
                    check_role = ro.Parent
                continue
    output = []
    us_keys = ["Id", "Name", "Role"]
    for us in users_li:
        if us.parent and us.parent > check_role:
            output.append({k: us.__dict__.get(k) for k in us_keys})
    # print(output)
    return output


if __name__ == "__main__":
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
    getSubOrdinates(4)
