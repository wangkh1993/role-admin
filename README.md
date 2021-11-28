# role-admin
A python application used to return list of users provided user ID as an input. 

## project Structure
```
magiclunch
├── Dockerfile
├── main
│   └── main.py
├── README.md
├── requirements.txt
├── test
│   ├── test_func.py
│   ├── test_getsub.py
│   └── __init__.py
```

## Files
`main.py`: application file, contains class modules and functions

`requirements.txt`: python dependencies

`test_func.py`: unittest for testing functions

`test_getsub.py`: unittest for testing getSubOridinates function

## Running using Docker
Required **Docker** installed. 
Run below command to build image:

```docker build -t --name=pickuser pickuser:latest .```

Run below command to fire up the container and start Python window:

```docker run -ti --name=pickuser pickuser```

In Python terminal within the container, run the import module:

```from main.main import *```

Now you can pass your input of roles, users, initiate objects and run function `getSubOridinates`, e.g.

```
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
ros = setRoles(roles)
uss = setUsers(users)
getSubOrdinates(1)
```

Sample output of above command:

```[{'Id': 2, 'Name': 'Emily Employee', 'Role': 4}, {'Id': 3, 'Name': 'Sam Supervisor', 'Role': 3}, {'Id': 4, 'Name': 'Mary Manager', 'Role': 2}, {'Id': 5, 'Name': 'Steve Trainer', 'Role': 5}]```

To run unittest use below command (when your container is running and called *picklunch*):

```docker exec -ti pickuser python -m unittest test/test_func.py```

Integration test using:

```docker exec -ti pickuser python -m unittest test/test_getsub.py```

## Running using local Python env
Module was built using Python 3.7. Use `pip` to install dependencies

```pip install -r requirements.txt```

Run below command using sample input provided in `main.py`

```python .\main\main.py```

Alternatively you can use interactive mode like the Docker example above.



