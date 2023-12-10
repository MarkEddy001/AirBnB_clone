#!/usr/bin/python3
"""
A module that contains the User class that
defines all  attributes/methods for a user object
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class that represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
