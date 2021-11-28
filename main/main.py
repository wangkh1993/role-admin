class Roles(object):
    """
    Class for Roles, getting an input dict of the role, initiate Id,Name and Parent attributes
    """
    def __init__(self, role):
        self.Id = role.get("Id")
        self.Name = role.get("Name")
        self.Parent = role.get("Parent")


class Users(object):
    """
    Class for Users, getting an input dict of the user, initiate Id,Name Role and parent attributes
    """
    def __init__(self, user):
        self.Id = user.get("Id")
        self.Name = user.get("Name")
        self.Role = user.get("Role")
        # Initiate parent attribute as None, fetching from roles later on
        self.parent = None

    def __str__(self):
        return str({"Id": self.Id, "Name": self.Name, "Role": self.Role})

# global variable
roles_li = []

def setRoles(roles_in):
    """
    Function to parse input list of dict into Roles object
    :param roles_in: list of dict
    :return: list, global variable
    """
    # access global variable
    global roles_li
    roles_li = [Roles(role_in) for role_in in roles_in]
    return None

# global variable
users_li = []


def setUsers(users_in):
    """
    Function to parse input list of dict into Users object
    :param users_in: list of dict
    :return: list, global variable
    """
    # access global variable
    global users_li
    users_li = [Users(user_in) for user_in in users_in]
    return None


def getSubOrdinates(user_id):
    """
    Given input of Roles and Users and UserId, find all the suboridinates' users
    :param user_id: int, user id
    :return: list of dict, users
    """
    check_role = 0
    # Iterate through Users, Roles, assign Roles'Parent attribute to each user, mark the Parent of the user matches to input user ID
    for us in users_li:
        for ro in roles_li:
            if us.Role == ro.Id:
                us.parent = ro.Parent
                if us.Id == user_id:
                    check_role = ro.Parent
                continue
    output = []
    # Define output Dict keys
    us_keys = ["Id", "Name", "Role"]
    for us in users_li:
        if us.parent and us.parent > check_role:
            output.append({k: us.__dict__.get(k) for k in us_keys})
    return output


if __name__ == "__main__":
    # sample input of roles and users
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
    print(output)
    # Expected
    # [{'Id': 2, 'Name': 'Emily Employee', 'Role': 4}, {'Id': 3, 'Name': 'Sam Supervisor', 'Role': 3}, {'Id': 5, 'Name': 'Steve Trainer', 'Role': 5}]
